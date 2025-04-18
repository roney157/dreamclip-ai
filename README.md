
# DreamClip.AI - Transforme texto em vídeo com IA (100% offline)

Este é o repositório oficial do **DreamClip.AI**! Um projeto simples que usa modelos locais para transformar texto em vídeo com narração sem depender de APIs.

---

## 🚀 Funcionalidades

- ✅ Gera vídeos a partir de texto com **Stable Video Diffusion** (exemplo dummy).
- ✅ Gera narração de texto com **Bark** (exemplo dummy).
- ✅ Combina áudio e vídeo com `ffmpeg`.
- ✅ Modo de teste automático: `python3 main.py --test`

---

## 📚 Requisitos

- Python 3.9+
- ffmpeg instalado.
- Ambiente com GPU (para modelos reais).

---

## 💻 Instalação

Clone o projeto e instale as dependências:

```bash
git clone https://github.com/seuusuario/dreamclip-ai.git
cd dreamclip-ai
pip install -r requirements.txt
```

---

## 🎬 Como usar

### 1. Teste automático (gera vídeo de exemplo)

```bash
python3 main.py --test
```
O vídeo será salvo em `output/final_video.mp4`.

---

### 2. Rodar como API

```bash
python3 main.py
```

Acesse:

```
http://localhost:10000/generate
```

Envie um JSON:

```json
{
    "text": "A beautiful sunset over the ocean."
}
```

O vídeo final será salvo em `output/final_video.mp4`.

---

## 🌍 Deploy no Render.com

1. Conecte este repositório ao Render.
2. Use:

- **Build Command:**
```bash
pip install -r requirements.txt
```

- **Start Command:**
```bash
python3 main.py
```

Obs: selecione um servidor com **GPU** para usar modelos reais.

---

## 🔥 Em breve

- Integração com modelos reais: Stable Video Diffusion + Bark.
- Geração de diferentes estilos visuais.

---

Feito com ❤️ para criação automática de vídeos com IA!
