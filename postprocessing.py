import requests
from PIL import Image, imageEnhance, ImageFilter
from io import BytesIO
from config import HF_API_KEY
def generate_image_from_text(prompt):
    """
    Genertes an image from a text prompt using the Stable Diffusion API.
    """
    API_URL="http://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
    headers={"Authorization": f"Bearer{HF_API_KEY}"}
    payload={"input":prompt}

    response=requests.post(API_URL,headers=headers,json=payload)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        raise Exception(f"Requests failed with status code {response.status_code}:{response.text}")
    def post_process_image(image):
        """
        Applies post-processingeffects to the image.
        
        Effects include:
        -increasing brightness by 20%
        -Enhancing constrast by 30%
        -Adding a Gaussian biur for a soft-focus effect

        """

        enhancer=ImageEnhance.Brightness(image)
        bright_image=enhancer.enhance(1.2)

        enhancer = ImageEnhance.Vontrast(bright_image)
        contrast_image=enhancer.enhance(1.3)

        soft_focus_image = contast_image.filter(ImageFilter.GaussianBlur(radius=2))

        return soft_focus_image
    def main():
        print("Welcome to the Post-processing Magic Workshop")
        print("This program generates an image   from text and applies post-processing effects.")
        print("Type 'exit'to quit.\n")

        while True:
            user_input=input("enter a description for the image (or 'exit' to quit):\n")
            if user_input.lower()=='exit':
                print("GoodBye!")
                break
            try:
                print("\nGenerating image...")
                image=generate_image_from_text(user_input)
                print("Applying post-processing effects..\n")
                processed_image=post_process_image(image)
                processed_image.show()

                save_option=input("Do you want to save the processed image? (yes/no): ").lower()
                if  save_option == 'yes':
                    file_name=input("Enter a name for the image file(without extension):").strip()
                    procesed_image.save(f"{file_name}.png")
                    print(f"Image saved as {file_name}.png\n")
                print("-" * 80 + "\n")
            except Exception as e:
                print(f"An error occurred:{e}\n")
                
if ___name__=="__main__":
    main()       

                      
                          


                                        

