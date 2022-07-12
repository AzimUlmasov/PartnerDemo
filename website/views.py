from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'en/home.html', {})

def about_us(request):
    return render(request, 'en/about_us.html', {})    

def company_info(request):
    return render(request, 'en/company_info.html', {})    

def msg_from_top_management(request):
    return render(request, 'en/msg_from_top_management.html', {})    

def management_philosophy(request):
    return render(request, 'en/management_philosophy.html', {})    

def corporate_profile(request):
    return render(request, 'en/corporate_profile.html', {})    

def about_our_business(request):
    return render(request, 'en/about_our_business.html', {})    

def organization(request):
    return render(request, 'en/organization.html', {})    

def global_network(request):
    return render(request, 'en/global_network.html', {})    

def our_team(request):
    return render(request, 'en/our_team.html', {})    

def products(request):
    return render(request, 'en/products.html', {})    

def material_industry(request):
    return render(request, 'en/material_industry.html', {})    

def daily_food_industry(request):
    return render(request, 'en/daily_food_industry.html', {})      

def automotive_and_commercial(request):
    return render(request, 'en/automotive_and_commercial.html', {})    

def medical(request):
    return render(request, 'en/medical.html', {})    

def consulting(request):
    return render(request, 'en/consulting.html', {})    

def dx(request):
    return render(request, 'en/dx.html', {})

def careers(request):
    return render(request, 'en/careers.html', {})   

def japan(request):
    return render(request, 'en/japan.html', {})    

def overseas(request):
    return render(request, 'en/overseas.html', {})        

def apply_now(request):
    return render(request, 'en/apply_now.html', {})

def contact(request):
    if request.method == "POST":
        your_name = request.POST ['your-name']
        your_email = request.POST ['your-name']
        your_phone = request.POST ['your-name']
        your_subject = request.POST ['your-name']
        your_message = request.POST ['your-name'] 
        # send an email
        '''
        send_mail(
            name,  # name
            email, # from email
            phone, # phone 
            subject, # subject
            message, # message
            ['azimulmasov2@gmail.com'], # To Email
            )  
        '''
        return render(request, 'en/contact.html', {
            'your_name': your_name,
            'your_email': your_email,
            'your_phone': your_phone,
            'your_subject': your_subject,
            'your_message': your_message
            }) 

    else:    
        return render(request, 'en/contact.html', {})        
    
def home_(request):
    return render(request, 'jp/home_.html', {})

def about_us_(request):
    return render(request, 'jp/about_us_.html', {})

def company_info_(request):
    return render(request, 'jp/company_info_.html', {})    

def msg_from_top_management_(request):
    return render(request, 'jp/msg_from_top_management_.html', {})    

def management_philosophy_(request):
    return render(request, 'jp/management_philosophy_.html', {})    

def corporate_profile_(request):
    return render(request, 'jp/corporate_profile_.html', {})    

def about_our_business_(request):
    return render(request, 'jp/about_our_business_.html', {})    

def organization_(request):
    return render(request, 'jp/organization_.html', {})    

def global_network_(request):
    return render(request, 'jp/global_network_.html', {})    

def our_team_(request):
    return render(request, 'jp/our_team_.html', {})    

def products_(request):
    return render(request, 'jp/products_.html', {})    

def material_industry_(request):
    return render(request, 'jp/material_industry_.html', {})    

def daily_food_industry_(request):
    return render(request, 'jp/daily_food_industry_.html', {})      

def automotive_and_commercial_(request):
    return render(request, 'jp/automotive_and_commercial_.html', {})    

def medical_(request):
    return render(request, 'jp/medical_.html', {})    

def consulting_(request):
    return render(request, 'jp/consulting_.html', {})    

def dx_(request):
    return render(request, 'jp/dx_.html', {})

def careers_(request):
    return render(request, 'jp/careers_.html', {})   

def japan_(request):
    return render(request, 'jp/japan_.html', {})    

def overseas_(request):
    return render(request, 'jp/overseas_.html', {})        

def apply_now_(request):
    return render(request, 'jp/apply_now_.html', {})          

def contact_(request):
    if request.method == "POST":
        your_name = request.POST ['your-name']
        your_email = request.POST ['your-name']
        your_phone = request.POST ['your-name']
        your_subject = request.POST ['your-name']
        your_message = request.POST ['your-name'] 
        # send an email
        '''
        send_mail(
            name,  # name
            email, # from email
            phone, # phone 
            subject, # subject
            message, # message
            ['azimulmasov2@gmail.com'], # To Email
            )  
        '''
        return render(request, 'jp/contact_.html', {
            'your_name': your_name,
            'your_email': your_email,
            'your_phone': your_phone,
            'your_subject': your_subject,
            'your_message': your_message
            }) 

    else:    
        return render(request, 'jp/contact_.html', {})    