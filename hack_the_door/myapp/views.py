from django.shortcuts import render, redirect
from .forms import StringForm

# ค่าสตริงที่ต้องการให้ผู้ใช้กรอก
SECRET_STRING = "django"

def input_view(request):
    if request.method == 'POST':
        form = StringForm(request.POST)
        if form.is_valid():
            input_string = form.cleaned_data['input_string']
            # ตรวจสอบว่า input_string ตรงกับ SECRET_STRING หรือไม่
            if input_string == SECRET_STRING:
                return redirect('success')  # ถ้าตรงให้ไปหน้า success
            else:
                form.add_error('input_string', 'Incorrect string! Try again.')  # ถ้าไม่ตรงให้แสดงข้อความผิด
    else:
        form = StringForm()
    return render(request, 'myapp/input_form.html', {'form': form})

def success_view(request):
    return render(request, 'myapp/success.html')
