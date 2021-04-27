from .models import Problem

from modeltranslation.translator import translator, TranslationOptions


class ProblemTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


translator.register(Problem, ProblemTranslationOptions)