## Practical 03 --Disambiguation 
### Report

#### 1. Tagger comparison

The aim of this Practical is to evaluate the performance of three different part of speech taggers working on the same dataset. 
The data for this analysis consists of a depedency treebank for finnish obtained from the [Universal Dependencies (UD) project](https://github.com/UniversalDependencies/UD_Finnish-TDT). This dataset was already in CoNLL-U format for ease of use and evaluation. The script for evaluating the performance of the taggers was downloaded from [CoNLL-2017 evaluation script] (http://universaldependencies.org/conll17/eval.zip). 

The first tagger for this analysis is UDPipe. UDPipe is a trainable pipeline for tagging CoNLL-U files. First, UDPipe was trained  with a dedicated Finnish dataset for training and available in the same Universal Dependency directory downloaded for this Practical. When in this directory, UDPipe was trained with the following command: `cat fi_tdt-ud-train.conllu | udpipe --tokenizer=none --parser=none --train fi.udpipe`. This produced a `fi.udpipe` file that was used for tagging a test Finnish file (available also in the the same Universal Dependency directory) by means of the following command `cat fi_tdt-ud-test.conllu | udpipe --tag fi.udpipe > fi_tdt-ud-test_output.conllu`. Finally, both the test file and the output file were ewvaluated using the evaluation script. The following Table 1 presents the results of the test.  

|Metrics    | Precision |    Recall |  F1 Score | AligndAcc|
|-----------|-----------|-----------|-----------|----------|
|Tokens     |    100.00 |    100.00 |    100.00 |          |
|Sentences  |    100.00 |    100.00 |    100.00 |          |
|Words      |    100.00 |    100.00 |    100.00 |          |
|UPOS       |     94.74 |     94.74 |     94.74 |     94.74|
|XPOS       |     95.89 |     95.89 |     95.89 |     95.89|
|Feats      |     91.00 |     91.00 |     91.00 |     91.00|
|AllTags    |     89.98 |     89.98 |     89.98 |     89.98|
|Lemmas     |     84.97 |     84.97 |     84.97 |     84.97|
|UAS        |    100.00 |    100.00 |    100.00 |    100.00|
|LAS        |    100.00 |    100.00 |    100.00 |    100.00|

Table 1. Evaluation results for Finnish UDPipe. 

Results of the evaluation show that UDPipe performs with a high F1 score of 94.74% for the UPOS (Universal Part of Speech) metrics. All other metrics report similar values for XPOS and Feats. AllTags and Lemmas metrics underperformed below 90%. 

The second tagger for this comparison consists of a [perceptron-based tagger](https://github.com/ftyers/conllu-perceptron-tagger) for CoNLL-U files intended as a teaching aid for this class. Similar to UDPipe, the tagger written in Python (tagger.py) was trained using the following command `cat fi_tdt-ud-train.conllu | python3 tagger.py -t model.dat`. A `model.dat` file was produced and it was used to predict the tagging functions of the test finnish dataset through the following command `cat fi_tdt-ud-test.conllu | python3 tagger.py model.dat > output`. Finally, the evaluation script was used and the results of the test are presented in Table 2. 


|Metrics    | Precision |    Recall |  F1 Score | AligndAcc |
|-----------|-----------|-----------|-----------|-----------|
|Tokens     |    100.00 |    100.00 |    100.00 |           |
|Sentences  |    100.00 |    100.00 |    100.00 |           | 
|Words      |    100.00 |    100.00 |    100.00 |           |
|UPOS       |     90.38 |     90.38 |     90.38 |     90.38 | 
|XPOS       |    100.00 |    100.00 |    100.00 |    100.00 |
|Feats      |    100.00 |    100.00 |    100.00 |    100.00 |
|AllTags    |     90.38 |     90.38 |     90.38 |     90.38 |
|Lemmas     |    100.00 |    100.00 |    100.00 |    100.00 | 
|UAS        |    100.00 |    100.00 |    100.00 |    100.00 |  
|LAS        |    100.00 |    100.00 |    100.00 |    100.00 |
Table 1. Evaluation results for the Finnish Perceptron-Based Tagger. 

Results for this evaluation show that the UPOS metrics were lower than those for UDPipe (F1 Score 90.38%). All other metrics increased considerably. 

The third tagger used for this comparison was [Hunpos](https://code.google.com/archive/p/hunpos/), a reimplementation of part-of-speech tagger by Thorsten Brants. Several issues appeared before attempting to inititate the tagger, including incompatibility with the Windows operating system and the inability to produce an appropriate model with the UD Finnish data. As a result, it was decided not to use Hunpos. 

Another effort was made to use NLTK. First, the Finnish data in CoNLL-U format was converted to raw text using a perl program from [UD Tools](https://github.com/universaldependencies/tools). The txt file was processed in NLTK and a tagged file was obtained with only POS tags. Then a CoNLL-U file was created Using a modified script aimed to tokenize sentence-segmented text. However, several errors were produced including the following error message:

Traceback (most recent call last):
  File "txtToConllu.py", line 28, in <module>
    print(index, i, upos[cnt][1], '_', '_', '_', '_', '_', '_', '_', '_')
IndexError: list index out of range

And: 
    
falconrr@FalconRR:~/IU_OneDrive/OneDrive_Intro_ to_CL/Disambiguation/tools$ python3 conll17_ud_eval.py --verbose fi_tdt-ud-test.conllu fintag.conllu
Traceback (most recent call last):
  File "conll17_ud_eval.py", line 506, in <module>
    main()
  File "conll17_ud_eval.py", line 484, in main
    evaluation = evaluate_wrapper(args)
  File "conll17_ud_eval.py", line 458, in evaluate_wrapper
    system_ud = load_conllu_file(args.system_file)
  File "conll17_ud_eval.py", line 453, in load_conllu_file
    return load_conllu(_file)
  File "conll17_ud_eval.py", line 170, in load_conllu
    raise UDError("There are multiple roots in a sentence")
__main__.UDError: There are multiple roots in a sentence

Clearly, more expertise is needed to create an acceptable CoNLL-U file for the evaluation script. Thus, no further attempts ensued. 

In conlusion, the UDPipe tagger produced the most accurate performance of the two programs compared. In the future, there is a need for more command on python and UDPipe.  

#### 3. Improve perceptron tagger

Following the instructions for this exercise, a [Spanish](https://github.com/UniversalDependencies/UD_Spanish-GSD) dataset was obtained from the Universal Dependencies project github repository. The UDPipe tagger was trained with the `es_gsd-ud-train.conllu` file and the tagger was run with the `pt_gsd-ud-test.conllu` data. Finally, the tagger was evaluated using the [CoNLL-2017 evaluation script] (http://universaldependencies.org/conll17/eval.zip). Table 3 shows the results of the test: 

|Metrics    | Precision |    Recall |  F1 Score | AligndAcc |
|-----------|-----------|-----------|-----------|-----------|
|Tokens     |    100.00 |    100.00 |    100.00 |           |
|Sentences  |    100.00 |    100.00 |    100.00 |           |
|Words      |    100.00 |    100.00 |    100.00 |           |
|UPOS       |     99.32 |     99.32 |     99.32 |     99.32 |
|XPOS       |    100.00 |    100.00 |    100.00 |    100.00 |
|Feats      |    100.00 |    100.00 |    100.00 |    100.00 | 
|AllTags    |     99.32 |     99.32 |     99.32 |     99.32 | 
|Lemmas     |    100.00 |    100.00 |    100.00 |    100.00 |
|UAS        |    100.00 |    100.00 |    100.00 |    100.00 |
|LAS        |    100.00 |    100.00 |    100.00 |    100.00 |
Table 3. Evaluation results for Spanish UDPipe test file. Note the high performance of the tagger. 

Subsequently, the same procedure was conducted with the `es_gsd-ud-dev.conllu` and results are shown in Table 4. 

|Metrics    | Precision |    Recall |  F1 Score | AligndAcc |
|:----------|:----------|:----------|:----------|:----------|
|Tokens     |    100.00 |    100.00 |    100.00 |           |
|Sentences  |    100.00 |    100.00 |    100.00 |           |
|Words      |    100.00 |    100.00 |    100.00 |           |
|UPOS       |     95.57 |     95.57 |     95.57 |     95.57 |
|XPOS       |    100.00 |    100.00 |    100.00 |    100.00 |
|Feats      |    100.00 |    100.00 |    100.00 |    100.00 |
|AllTags    |     95.57 |     95.57 |     95.57 |     95.57 |
|Lemmas     |    100.00 |    100.00 |    100.00 |    100.00 |
|UAS        |    100.00 |    100.00 |    100.00 |    100.00 |
|LAS        |    100.00 |    100.00 |    100.00 |    100.00 |

Table 4. Evaluation results for Spanish UDPipe dev file. Note the decreasing performance of the tagger. 

In an attempt to improve the F1 score of the tagger with the dev file, the `by _get_features()` in the `tagger.py` script was modified. First, add('i suffix', word[-3:]) was modified to different values (i.e. word[-5:], word[-2:], word[-3:2], etc.) but tagger was underperforming with a F1 score of 93. When add('i pref1', word[0]) was changed, an error message appear signaling the index out of range. As a result, this was left untouched. Then, a '2' and '4' was added to the function ('i-1 suffix', context[i-2][-3:4]) and the tagger decreased slightly its F1 Score (95.34). Any further attempts with the other variables produced an error with the index out of range. A final attempt to produce an improved change, it was added a new index for all suffixes ([-3:1]) but results the tagger failed to improve. 

In conclusion, any attempt to modify the script produced a reduction in the performance of the tagger. Thus, it can be concluded that this tagger has the optimum level of performance for Spanish. 