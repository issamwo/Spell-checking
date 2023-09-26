from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline, TFBartForConditionalGeneration
from spellchecker import SpellChecker

from .conf import SPELL_CHECKER_HUGGINGFACE_MODEL_NAME, FIX_SPELLING_HUGGINGFACE_MODEL_NAME, TASK, MAX_LENGTH



class SpellCorrection(object):
    """Correct spelling

    model_name: str
                model used to analyse text sentiment (models are from huggingface)

    """

    def __init__(self) -> None:
        # Method 1:
        self.tokenizer = AutoTokenizer.from_pretrained(SPELL_CHECKER_HUGGINGFACE_MODEL_NAME)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(SPELL_CHECKER_HUGGINGFACE_MODEL_NAME)
        # Method 3:
        self.fix_spelling_pipeline = pipeline(TASK, model=FIX_SPELLING_HUGGINGFACE_MODEL_NAME)

    
    def correct_spelling(self, inputs: str) -> str:
        """inspect inputs and return the correct spelling

        Args:
            inputs (str): token to be inspected

        Returns:
            str: correct spelling of inputs
        """
        input_ids = self.tokenizer.encode(inputs,return_tensors='pt')
        sample_output = self.model.generate(
            input_ids,
            do_sample=True,
            max_length=MAX_LENGTH,
            top_p=0.99,
            num_return_sequences=1
        )
        res = self.tokenizer.decode(sample_output[0], skip_special_tokens=True)
        return res


    def spell_checker(self, inputs: str):
        """Check if spelling is known

        Args:
            inputs (str): text

        Returns:
            _type_: input corrected
        """
    
        spell = SpellChecker()

        # Split the text into words
        words = inputs.split()

        # Find and correct misspelled words
        corrected_text = []
        for word in words:
            # Check if the word is misspelled
            if spell.unknown([word]):
                # print("unknown word = ", word)
                # Get the most likely correction for the misspelled word
                corrected_word = spell.correction(word)
                if corrected_word==None:
                    corrected_word= word
                #print("correcte word = ", corrected_word)
                corrected_text.append(corrected_word)
            else:
                corrected_text.append(word)

        # Reconstruct the corrected text
        corrected_text = " ".join(corrected_text)

        return corrected_text

    
    def fix_spelling(self, text):
        """Fix spelling using a text2text generation task 

        Args:
            text (_type_): text to be corrected

        Returns:
            _type_: text corrected
        """
        text_corrected = self.fix_spelling_pipeline("fix:"+text, max_length = MAX_LENGTH)
        return text_corrected[0]["generated_text"]
        

