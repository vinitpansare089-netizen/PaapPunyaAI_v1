# LLM Benchmark — PaapPunyaAI

## Hardware

CPU: Intel Core i5-1035G1
GPU: Intel UHD Graphics
Inference: CPU

## Test Question

"Should I lie to help my friend?"

## Pipeline

User Question
→ Embedding
→ FAISS Retrieval
→ Prompt Construction
→ Ollama LLM
→ Response

## Results

| Model | Parameters | LLM Time | Observation |
|---|---:|---:|---|
| Phi-3 | 3.8B | 146.58s | Best quality, too slow |
| Llama 3.2 | 1B | 35.59s | Faster, acceptable quality |
| Qwen 2.5 | 0.5B | 23.05s | Fastest, weaker reasoning |

## RAG Pipeline Timing

Embedding: ~0.05s
Retrieval: ~0.00s
Prompt: ~0.00s

The primary bottleneck was LLM inference.

## Decision

For local development, Qwen 2.5 0.5B provides the fastest response time on the available CPU hardware.

However, model quality must also be considered before selecting the production model.

## Engineering Lesson

Do not optimize the entire pipeline blindly.

Measure each stage first.

In PaapPunyaAI, retrieval was already fast. LLM inference was the dominant bottleneck.