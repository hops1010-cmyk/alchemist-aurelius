# kaggle_cover_gen.py
# Run on Kaggle (GPU) to generate the Aurelius front cover.
# pip install diffusers transformers accelerate safetensors

from diffusers import StableDiffusionPipeline
import torch

prompt = ("Book cover, fantasy novel 'The Alchemist: Aurelius', "
          "a wise alchemist in royal robes held captive in a grand castle, "
          "glowing orange light, dark navy and gold palette, "
          "small kitten named Furball, cinematic, high detail")

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
).to("cuda")

image = pipe(prompt, num_inference_steps=30).images[0]
image.save("cover.png")
print("saved cover.png")
