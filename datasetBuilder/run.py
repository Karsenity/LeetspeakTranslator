from datasetBuilder.generate_phrases import GeneratePhrases

generator = GeneratePhrases("../Resources/dialogs.txt")
[print(i) for i in generator.apply_leetspeak(2)]