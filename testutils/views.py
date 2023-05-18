from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext = request.GET.get('text','default')
    tremovepunc= request.GET.get('removepunc','off')
    tfullcaps= request.GET.get('fullcaps','off')
    tnewlineremover= request.GET.get('newlineremover','off')
    tspaceremover= request.GET.get('spaceremover','off')
    tcharcnt= request.GET.get('charcnt','off')

    tlowercase = request.GET.get('lowercase', 'off')
    tincfontsz = request.GET.get('incfontsz', 'off')
    tdecfontsz = request.GET.get('decfontsz', 'off')
    tbold = request.GET.get('bold', 'off')
    titalic = request.GET.get('italic', 'off')
    tunder = request.GET.get('under', 'off')
    twrdcnt = request.GET.get('wrdcnt', 'off')
    tlinecnt = request.GET.get('linecnt', 'off')
    tlong = request.GET.get('long', 'off')
    tsmall = request.GET.get('small', 'off')
    tcommon = request.GET.get('common', 'off')
    tsome = request.GET.get('some', 'off')
    tdupe = request.GET.get('dupe', 'off')
    
    print(djtext)
    print(tremovepunc)
    if tremovepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params= {'Purpose': 'Remove Punctuations', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    if tnewlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n':
                analyzed = analyzed + char
        params= {'Purpose': 'new line remove', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)  
    if tfullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params= {'Purpose': 'Uppercase', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    if tspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params= {'Purpose': 'Extra Space Remove', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
       
    if tcharcnt == "on":
        # Compute character count
        analyzed = len(djtext)
        params = {'Purpose': 'Character Count', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    if tlowercase == "on":
        # Convert to lowercase
        analyzed = djtext.lower()
        params = {'Purpose': 'Lowercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    if twrdcnt == "on":
        # Compute word count
        words = djtext.split()
        analyzed = len(words)
        params = {'Purpose': 'Word Count', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    if tlinecnt == "on":
        # Compute number of lines
        lines = djtext.split('\n')
        analyzed = len(lines)
        params = {'Purpose': 'Line Count', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    if tlong == "on":
        # Find the longest word
        words = djtext.split()
        longest_word = max(words, key=len)
        analyzed = longest_word
        params = {'Purpose': 'Longest Word', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    if tsmall == "on":
        # Find the smallest word
        words = djtext.split()
        smallest_word = min(words, key=len)
        analyzed = smallest_word
        params = {'Purpose': 'Smallest Word', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    if tcommon == "on":
        # Find the most common word
        words = djtext.split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        most_common_word = max(word_count, key=word_count.get)
        analyzed = most_common_word
        params = {'Purpose': 'Most Common Word', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    if tsome == "on":
        # Find the least common word
        words = djtext.split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        least_common_word = min(word_count, key=word_count.get)
        analyzed = least_common_word
        params = {'Purpose': 'Least Common Word', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    
    return HttpResponse("Error")