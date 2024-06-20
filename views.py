from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from . import regression as pass1
def home(request):
    k=''
    p=''
    c="yellow"
    model='k'
    temp=loader.get_template("home.html")
    if request.method=='POST':
        print(request.POST)
        s=request.POST.copy()
        k=s['news']
        print(k)
        # return redirect('home')
        if s['news']=='':
            return HttpResponse(temp.render({'result':"ENTER NEWS","news":"","code":"Black"},request))
        if s['model']=='':
            return HttpResponse(temp.render({'result':"SELECT MODEL","news":k,"code":"Black"},request))
        if s['model']=='RF':
            result=pass1.predict_RF(s['news'])
        elif s['model']=="LR":
            result=pass1.predict_LG(s['news'])
        elif s['model']=="SVM":
            result=pass1.predict_SVM(s['news'])
        else:
            result=pass1.predict_PAC(s['news'])
        if result==1:
            p="TRUE NEWS"
            c="green"
        elif result==0:
            p="FAKE NEWS"
            c="red"
        model=s['model']
    context={
        'result':p,
        "news": k,
        "code":c,
        "model":model
    }
    return HttpResponse(temp.render(context,request))
# Create your views here.
