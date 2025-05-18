import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image # For image handling

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found. Make sure it's set in your .env file or environment variables.")

genai.configure(api_key=API_KEY)

# --- Example 1: Analyzing a textual defect description ---
def analyze_defect_description_with_gemini(description):
    """Uses Gemini to analyze a textual defect description."""
    try:
        # Choose a model. 'gemini-1.5-flash' is fast and capable for many tasks.
        # 'gemini-pro' or 'gemini-1.5-pro' might be used for more complex reasoning.
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        prompt = f"""Analyze the following manufacturing defect description:
        "{description}"

        Provide:
        1. A concise summary of the defect.
        2. Three potential root causes (e.g., machine error, material flaw, operator mistake).
        3. Two suggested immediate actions for quality control personnel.
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error in analyze_defect_description_with_gemini: {e}")
        return None

# --- Example 2: Analyzing an image for defects with Gemini (Multimodal) ---
def analyze_image_defect_with_gemini(image_path, user_prompt):
    """Sends an image and a prompt to a multimodal Gemini model for defect analysis."""
    try:
        # Ensure you use a model that supports image input, e.g., 'gemini-1.5-flash-latest' or 'gemini-pro-vision'
        # The 'latest' tag usually points to a recent stable version.
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        if not image_path: # Handle case where no image is provided
            return "Image path is missing."

        # Check if the image exists
        if not os.path.exists(image_path):
             return f"Image not found at path: {image_path}"

        # Attempt to open the image to ensure it's valid before sending to API
        try:
            img = Image.open(image_path)
        except Exception as e:
            return f"Error opening image {image_path}: {e}"

        # The generate_content method can take a list of parts (text, image)
        response = model.generate_content([user_prompt, img])
        return response.text
    except google.generativeai.types.generation_types.BlockedPromptException as bpe:
        print(f"Image analysis blocked by API: {bpe}")
        return "The image analysis request was blocked. This might be due to safety settings or image content."
    except Exception as e:
        print(f"Error in analyze_image_defect_with_gemini: {e}")
        return f"An error occurred during image analysis: {str(e)}"


if __name__ == "__main__":
    print("--- Gemini API for Quality Control Demo ---")

    # Textual analysis example
    defect_text = "The casing for product SN789 shows multiple hairline cracks near the hinge assembly. Unit was processed on Line B, shift 2."
    print(f"\nAnalyzing defect description: '{defect_text}'")
    text_analysis_result = analyze_defect_description_with_gemini(defect_text)
    if text_analysis_result:
        print("\nGemini Text Analysis Result:")
        print(text_analysis_result)
    else:
        print("Could not get text analysis result.")

    # Image analysis example
    # Create a dummy image for demonstration purposes
    dummy_image_path = "dummy_product_image.png"
    try:
        img = Image.new('RGB', (200, 150), color = 'skyblue')
        # Let's add a "defect" (a red square)
        for x in range(50, 80):
            for y in range(60, 80):
                img.putpixel((x, y), (255, 0, 0)) # Red color
        img.save(dummy_image_path)
        print(f"\nCreated a dummy image with a 'defect': {dummy_image_path}")

        image_prompt = "This is an image of a manufactured part. Describe any visible defects, their location, and potential severity (e.g., minor, major, critical)."
        print(f"\nAnalyzing image '{dummy_image_path}' with prompt: '{image_prompt}'")
        image_analysis_result = analyze_image_defect_with_gemini(dummy_image_path, image_prompt)

        if image_analysis_result:
            print("\nGemini Image Analysis Result:")
            print(image_analysis_result)
        else:
            print("Could not get image analysis result.")

    except ImportError:
        print("\nPillow library not installed. Skipping image creation/analysis for the demo.")
    except Exception as e:
        print(f"\nAn error occurred during the image example: {e}")
    finally:
        if os.path.exists(dummy_image_path):
            os.remove(dummy_image_path)
            print(f"\nCleaned up dummy image: {dummy_image_path}")