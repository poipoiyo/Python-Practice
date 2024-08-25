# Return search keyword
print("The program is to return search words from input url. \n")

samples = [
    ["https://www.youtube.com/results?search_query=LiSA-ADAMAS", "LiSA-ADAMAS"],
    ["youtube.com/results?search_query=YOASOBI+-+Idol", "YOASOBI - Idol"],
    ["www.youtube.com/results?search_query=I+want+it+that+way", "I want it that way"],
    ["https://www.youtube.com/results?search_query=%2B-+*%25", "+- *%"],
    ["https://ani.gamer.com.tw/search.php?keyword=LiSA-ADAMAS", "LiSA-ADAMAS"],
    ["ani.gamer.com.tw/search.php?keyword=YOASOBI+-+Idol", "YOASOBI - Idol"],
    ["https://ani.gamer.com.tw/search.php?keyword=%2B-+%2A%25", "+- *%"]
]
# https://www.w3schools.com/tags/ref_urlencode.ASP

youtube_keyword = "youtube.com"
baha_keyword = "ani.gamer.com.tw"
_url_encode_dict = {'%2B': '+', '%2A': '*','%25': '%'}

for sample in samples:
    _input = sample[0]
    _expect_output = sample[1]
    _answer = ""
    print("Input : ", _input)
    print("Expect out : ", _expect_output)

    if youtube_keyword in _input:
        _answer = _input.partition('=')[-1].replace('+', ' ')
        for key in _url_encode_dict:
            _answer = _answer.replace(key, _url_encode_dict[key])

    elif baha_keyword in _input:
        _answer = _input.partition('=')[-1].replace('+', ' ')
        for key in _url_encode_dict:
            _answer = _answer.replace(key, _url_encode_dict[key])

    print("Answer : ", _answer)

    _check = "correct" if _answer == _expect_output else "wrong"
    print("The answer is %s! \n" % _check)

