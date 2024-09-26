from django.shortcuts import render,redirect
from weva_drive import models
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.sessions.models import Session
def admin_dashboard(request):
    return render(request,"admin/admin.html")
def new_req(request):
    reg=models.Sam.objects.raw("SELECT * FROM sam JOIN login AS l ON sam.email = l.user_name WHERE l.status = 'inactive'")
    context={
        'rlist':reg
    }
    # Create your views here.
    return render(request,'service_providers/new_request.html',context)
def approve_request(request,rid):
    reg=models.Sam.objects.get(reg_id=rid)
    email_id=reg.email
    log=models.Login.objects.get(user_name=email_id)
    log.status='active'
    log.save()
    return redirect("new_req")
def reject_request(request,rid):
    reg=models.Sam.objects.get(reg_id=rid)
    email_id=reg.email
    log=models.Login.objects.get(user_name=email_id)
    log.status='rejected'
    log.save()
    return redirect("new_req") 
def search(request):
    stat=request.POST['sel']
    log=models.Sam.objects.raw("SELECT * FROM sam as t JOIN login AS l ON t.email = l.user_name WHERE l.user_type='service_provider' and l.status = %s",[stat])
    context={
        'rlist':log
     }
    return render(request,'service_providers/new_request.html',context)

def update_password(request)    :
    return render(request,"update_password/update_password.html")

def new_password(request):
    npass=request.POST['pass']
    cpass=request.POST['cpass']
    if npass==cpass:
        uname=request.session['semail']
        log=models.Login.objects.get(user_name=uname)
        log.password=npass
        log.save()
        return redirect("login")
    else :
        return redirect("update_password")
def category(request):
    categ=models.Cat.objects.all()
    context={
            'clist':categ
        }
    return render(request,'category/category.html',context)

def save_cat(request):
    name=request.POST['cname']
    le=models.Cat.objects.filter(cat_name=name)
    if len(le)==0:
        reg=models.Cat(cat_name=name)
        reg.cat_name=name
        reg.save()
        messages.success(request,"saved successfully")
        return redirect("category")
    else:
        messages.warning(request,"Category already exists")
        return redirect("category")
        return HttpResponse('try another category')
         
def update_cat(request):
    name=request.POST['cname']
    id=request.POST['cat_id']
    reg=models.Cat.objects.get(cat_id=id)
    reg.cat_name=name
    reg.save()
    return redirect("category")
def cat_edit(request,cat_id):
    categ=models.Cat.objects.get(cat_id=cat_id)
    context={
        'cdata':categ
    }
    return render(request,"category/cat_edit.html",context)
    
def cat_delete(request,cat_id):
    categ=models.Cat.objects.get(cat_id=cat_id)
    ct=models.Projects.objects.filter(fk_cat_id=cat_id).count()
    if ct==0:
        categ.delete()
        messages.success(request,"Category deleted successfully.")
    else:
        messages.error(request, "Cannot delete category because it is being used in a project.")
    return redirect("category")
def pack_view(request):
    categ=models.Package.objects.all()
    context={
            'plist':categ
        }
    return render(request,"package/pack.html",context)

def p_edit(request,package_id):
    categ=models.Package.objects.get(package_id=package_id)
    context={
        'plist':categ
    }
    return render(request,"package/edit_pack.html",context)
def save_pack(request):
    name=request.POST['cname']
    dur=request.POST['sel']
    rate=request.POST['rate']
    le=models.Package.objects.filter(packagename=name)
    if len(le)==0:
        reg=models.Package(packagename=name)    
        reg.packagename=name
        reg.duration=dur
        reg.rate=rate
        reg.actions='inactive'
        reg.save()
        categ=models.Package.objects.all()
        context={
                'plist':categ
            }
        messages.success(request,"saved successfully") 
        return redirect("pack_view")      
    else:
        messages.warning(request,"package already exists")
        return redirect("pack_view")
        return HttpResponse("try a different package")
       
def p_delete(request,package_id):
    categ=models.Package.objects.get(package_id=package_id)
    ct=models.ServiceproviderPayment.objects.filter(fk_pack_id=package_id).count()
    if ct==0:
        categ.delete()
        messages.success(request,"category deleted successsfully")
    else:
        messages.error(request,"cannot delete.package exists in payment")
    return redirect("pack_view")
    
def update_pack(request):
    name=request.POST['cname']
    id=request.POST['package_id']
    dur=request.POST['dur']
    rate=request.POST['rate']
    actions=request.POST['actions']
    reg=models.Package.objects.get(package_id=id)
    reg.package_id=id
    reg.packagename=name
    reg.duration=dur
    reg.rate=rate
    reg.actions=actions
    reg.save()
    return redirect("pack_view")
def paid(request):
    log=models.ServiceproviderPayment.objects.raw("SELECT * FROM serviceprovider_payment AS s JOIN sam  ON sam.email = s.se_email join package as p on p.package_id=s.fk_pack_id WHERE  s.status = 'paid'")
    context={
        'rlist':log
    }
    return render(request,"paid_service/paid_service_providers.html",context)
def free(request):
    log=models.Sam.objects.filter(status__isnull=True)
    context={
        'rlist':log
    }
    return render(request,"paid_service/unpaid_service_providers.html",context)
def portfolio(request):
    return render(request,'portfolio/portfolio.html')
def search_port(request):
    stat=request.POST['sel']
    log=models.Projects.objects.raw("SELECT * FROM projects as p join portfolio as po on p.proj_id=po.fk_prj_id where po.status=%s",[stat])
    context={
        'rlist':log
    }
    return render(request,"portfolio/portfolio.html",context)
def p_approve_request(request,portfolio_id):
    reg=models.Portfolio.objects.get(portfolio_id=portfolio_id)    
    reg.status='Approved'
    reg.save()
    return redirect("portfolio")
def p_reject_request(request,portfolio_id):
    reg=models.Portfolio.objects.get(portfolio_id=portfolio_id)    
    reg.status='Rejected'
    reg.save()
    return redirect("portfolio")

def details(request,portfolio_id):
    
    reg=models.Portfolio.objects.raw("SELECT * FROM Projects AS p JOIN Portfolio AS po ON p.proj_id = po.fk_prj_id JOIN sam ON sam.reg_id = p.fk_reg_id where po.portfolio_id=%s and sam.user_type='service_provider'",[portfolio_id])
    
    context={
        'rlist':reg
    }
    return render(request,"portfolio/view_details.html",context)
def gallery_port(request,pi):
     
    portfolio=models.Portfolio.objects.get(portfolio_id=pi)
    gallery=models.Gallery.objects.filter(fk_portfolio_id=pi)
    context={
        'portfolio':portfolio,
        'gallery_list':gallery
    }
    return render(request,"portfolio/image.html",context)


def dashboard(request):
    return render(request,"admin/admin.html")
def cl(request):
    log=models.Sam.objects.filter(user_type='client')
    context={
        'rlist':log
    }
    return render(request,"portfolio/client.html",context)
def reason(request,gid):
    reg=models.Gallery.objects.get(gallery_id=gid)    
    context={
        'image_id':gid
    }
    return render(request,"portfolio/reject.html",context)
def approve_image(request,gid):
    reg=models.Gallery.objects.get(gallery_id=gid)    
    reg.status='active'
    reg.save()
    return redirect("portfolio")
def logout(request):
    Session.objects.all().delete()
    return render(request,"index.html")
def reject_image(request):
    gid=request.POST['gallery_id']
    mes=request.POST['reason']

    reg=models.Gallery.objects.get(gallery_id=gid)    
    reg.status='rejected'
    reg.feedback=mes
    reg.save()
    return redirect("portfolio")