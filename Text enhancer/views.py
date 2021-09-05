from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get("text","default")
    removepunc = request.GET.get("removepunc","off")
    Capitalize = request.GET.get("Capitalize","off")
    Newlineremover = request.GET.get("Newlineremover","off")
    Extra_Space_Remover = request.GET.get("Extra Space Remover","off")
    analyzed = djtext
    params = {'purpose':None, 'analyzedtext': analyzed}

    if removepunc == 'on':
        punc = '''!()-[]{}:;'"\,<>./?@#$%*_'''

        analyzed = ''
        for char in params['analyzedtext']:
            if char not in punc:
                analyzed = analyzed + char
        params['analyzedtext'] = analyzed
        if params['purpose']:
            params['purpose'] = params['purpose'] + ', Removed Punctuations'
        else:
            params['purpose'] =' Removed Punctuations'
    if Capitalize == 'on':
        analyzed = ''
        for char in params['analyzedtext']:
                analyzed = analyzed + char.upper()
        params['analyzedtext'] = analyzed
        if params['purpose']:
            params['purpose'] = params['purpose'] + ', Capitalized all characters'
        else:
            params['purpose'] = ' Capitalized all characters'
    if Newlineremover == 'on':
        analyzed = ''
        for char in params['analyzedtext']:
            if char != "\n" and char != '\r':
                analyzed = analyzed + char

        params['analyzedtext'] = analyzed
        if params['purpose']:
            params['purpose'] = params['purpose'] + ', All New lines removed'
        else:
            params['purpose'] =' All New lines removed'

    if Extra_Space_Remover == 'on':
        analyzed = ''
        for index,char in enumerate(params['analyzedtext']):
            if djtext[index] == " " and djtext[index-1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params['analyzedtext'] = analyzed
        if params['purpose']:
            params['purpose'] = params['purpose'] + ', Extra Spaces Removed'
        else:
            params['purpose'] = ' Extra Spaces Removed'


    elif removepunc == 'off' and Extra_Space_Remover == 'off' and Newlineremover == 'off' and Capitalize == 'off' :
        params['analyzedtext'] = 'Please Select any operation'
    return render(request, 'analyze.html', params)


