# Se sugiere ingresar a este sitio:
# https://bbycroft.net/llm
# Para ver una simulación de modelos LLM

"""
Aquí encontrarán una demo de un transformer que aprende cómo ordenar las letras A, B, C que se mencionan en la Web

Nota: instalar torch, una librería de ML y deep learning
pip install torch
"""

# tiny_transformer_sort.py
# Un Transformer MUY pequeño que aprende a ordenar secuencias con letras {A,B,C}.
# Autor: para uso didáctico :)

import random
import torch
import torch.nn as nn
import torch.nn.functional as F

# ---------- Config ----------
VOCAB = ["A", "B", "C"]
stoi = {c: i for i, c in enumerate(VOCAB)}
itos = {i: c for c, i in stoi.items()}

SEQ_LEN = 6  # p.ej. C B A B B C
EMBED_DIM = 32
NUM_HEADS = 2
FF_DIM = 64
LR = 2e-3
EPOCHS = 2000  # baja si querés ver algo rápido
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
BATCH = 128
PRINT_EVERY = 200


# ---------- Datos ----------
def gen_sample(seq_len=SEQ_LEN):
    # Genera una secuencia aleatoria y su versión ORDENADA
    xs = [random.randint(0, len(VOCAB) - 1) for _ in range(seq_len)]
    ys = sorted(xs)  # objetivo: la secuencia ordenada
    return xs, ys


def make_batch(batch_size=BATCH):
    xs, ys = [], []
    for _ in range(batch_size):
        x, y = gen_sample()
        xs.append(x)
        ys.append(y)
    x = torch.tensor(xs, dtype=torch.long, device=DEVICE)  # (B, T)
    y = torch.tensor(ys, dtype=torch.long, device=DEVICE)  # (B, T) etiquetas por posición
    return x, y


# ---------- Modelo ----------
class TinySorter(nn.Module):
    def __init__(
        self,
        vocab_size=len(VOCAB),
        embed_dim=EMBED_DIM,
        n_heads=NUM_HEADS,
        ff_dim=FF_DIM,
        seq_len=SEQ_LEN,
    ):
        super().__init__()
        self.tok = nn.Embedding(vocab_size, embed_dim)
        self.pos = nn.Embedding(seq_len, embed_dim)

        self.attn = nn.MultiheadAttention(embed_dim, n_heads, batch_first=True)
        self.ln1 = nn.LayerNorm(embed_dim)

        self.ffn = nn.Sequential(
            nn.Linear(embed_dim, ff_dim),
            nn.GELU(),
            nn.Linear(ff_dim, embed_dim),
        )
        self.ln2 = nn.LayerNorm(embed_dim)

        self.head = nn.Linear(embed_dim, vocab_size)  # logits por posición

    def forward(self, x):  # x: (B, T)
        B, T = x.shape
        tok = self.tok(x)  # (B, T, D)
        pos_idx = torch.arange(T, device=x.device).unsqueeze(0).expand(B, T)
        pos = self.pos(pos_idx)  # (B, T, D)
        h = tok + pos

        # Self-attention (no causal; queremos leer toda la secuencia para ordenarla)
        h2, _ = self.attn(h, h, h)  # (B, T, D)
        h = self.ln1(h + h2)

        # Feed-forward
        h2 = self.ffn(h)  # (B, T, D)
        h = self.ln2(h + h2)

        logits = self.head(h)  # (B, T, vocab)
        return logits


# ---------- Entrenamiento ----------
def train():
    model = TinySorter().to(DEVICE)
    opt = torch.optim.AdamW(model.parameters(), lr=LR)

    for epoch in range(1, EPOCHS + 1):
        model.train()
        x, y = make_batch()
        logits = model(x)  # (B, T, V)
        loss = F.cross_entropy(logits.view(-1, len(VOCAB)), y.view(-1))  # (B*T, V)  # (B*T)

        opt.zero_grad()
        loss.backward()
        opt.step()

        if epoch % PRINT_EVERY == 0:
            model.eval()
            # Prueba con un ejemplo fijo: C B A B B C
            test = torch.tensor([[stoi[c] for c in ["C", "B", "A", "B", "B", "C"]]], device=DEVICE)
            with torch.no_grad():
                pred = model(test).argmax(-1)[0].tolist()
            seq_in = " ".join(["C", "B", "A", "B", "B", "C"])
            seq_out = " ".join(itos[i] for i in pred)
            print(f"[{epoch:4d}] loss={loss.item():.4f} | IN: {seq_in}  -> PRED: {seq_out}")

    return model


# ---------- Inferencia ----------
def infer(model, seq):
    x = torch.tensor([[stoi[c] for c in seq]], device=DEVICE)
    with torch.no_grad():
        pred = model(x).argmax(-1)[0].tolist()
    return [itos[i] for i in pred]


if __name__ == "__main__":
    model = train()
    # Demo final
    demo = ["C", "B", "A", "B", "B", "C"]
    print("Entrada: ", " ".join(demo))
    print("Salida : ", " ".join(infer(model, demo)))
