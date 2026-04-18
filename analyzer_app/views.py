from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from analyzer_app.utils.text_extractor import extract_pdf_text, extract_docx_text
from nlp_module.analyzer import analyze_resume

# Create your views here.
def home(request):
    return render(request,'index.html')

@csrf_exempt
def analyze(request):
    if request.method == 'POST':
        try:
            if 'resume_file' in request.FILES:
                resume_file = request.FILES['resume_file']
                if resume_file.name.endswith('.pdf'):
                    resume_text = extract_pdf_text(resume_file)
                elif resume_file.name.endswith('.docx'):
                    resume_text = extract_docx_text(resume_file)
                else:
                    return JsonResponse({'error':'Unsupported File Format'},status=400)
            else:
                resume_text = request.POST.get('resume_text','')
            
            jd_text = request.POST.get('jd_text','')

            if not resume_text and not jd_text:
                return JsonResponse({
                    'error':'Both resume and jd required'
                },status=400)
            
            result = analyze_resume(resume_text,jd_text)

            return JsonResponse(result)
        
        except Exception as e:
            return JsonResponse({
                'error':str(e)
            },status=500)
        
    return render(request,'index.html')