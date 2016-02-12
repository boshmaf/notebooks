# Copyright (c) 2016 Yazan Boshmaf
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.


import warnings
warnings.filterwarnings('ignore')

from sklearn.feature_extraction import DictVectorizer


def get_vector(name, feature_names, full_vector):
    """
    Returns a complete feature vector
    """
    name_features = {}
    name_features["last_letter"] = name[-1]
    name_features["last_two"] = name[-2:]
    name_features["last_is_vowel"] = 0 if name[-1] in "aeiouy" else 0

    vectorizer = DictVectorizer()
    small_vector = vectorizer.fit_transform(name_features).toarray()[0]
    small_feature_names = vectorizer.get_feature_names()

    hit_count = 0
    for index, feature_name in enumerate(feature_names):
        if feature_name in small_feature_names:
            full_vector[index] = small_vector[small_feature_names.index(feature_name)]
            hit_count += 1
        else:
            full_vector[index] = 0

    assert hit_count == len(small_feature_names) == small_vector.shape[0]
    assert full_vector.shape[0] == len(feature_names)

    return full_vector
