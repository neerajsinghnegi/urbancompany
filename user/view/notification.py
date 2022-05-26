from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from user.models import Profile , Services , Categorys , Employee , Choose 
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def notification(req ):

    # it check user login with admin account 
    user_obj = req.user
    profile_obj = Profile.objects.filter(user = user_obj).first()
    if profile_obj is None:
        return redirect('/login')

    # it take all objects of employee with the same userid
    emp_obj = Employee.objects.filter(user_id = user_obj.id).all()
    userlist = []
    for emp in emp_obj:

        # it take all objects of choose with employee id same
        order_obj = Choose.objects.filter(emp_id=emp.id , cart = False).all().order_by("-order_date")
        for order in order_obj:

            user_id = order.user_id
            print(user_id)
            user_obj = User.objects.filter(pk = user_id).first()
            print(user_obj)
            name = user_obj.username

            # it store all data in dictionary
            Disc={"name":name,"cost":emp.cost,"category":emp.category,"service":emp.service,"address":order.address,"status":order.status,"orderid":order.id,"datetime":order.order_date}
            userlist.append(Disc)

    # it sort data according to data and time
    userlist = sorted(userlist, key = lambda i: i['datetime'] , reverse=True)
            

    return render(req , 'user/notification.html' , {"present":len(userlist),"users":userlist})


@login_required(login_url='/login')
def decline(req , order_pk):
    user_obj = req.user
    profile_obj = Profile.objects.filter(user = user_obj).first()
    if profile_obj is None:
        return redirect('/login')

    # it change the status to canceled
    order_obj = Choose.objects.filter(pk=order_pk).first()
    order_obj.status = "Canceled"
    order_obj.save()

    return redirect("/notification")


@login_required(login_url='/login')
def accept(req , order_pk):
    user_obj = req.user
    profile_obj = Profile.objects.filter(user = user_obj).first()
    if profile_obj is None:
        return redirect('/login')

    
    # it change the status to approved
    order_obj = Choose.objects.filter(pk=order_pk).first()
    order_obj.status = "Approved"
    order_obj.save()

    return redirect("/notification")