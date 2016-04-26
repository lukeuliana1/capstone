from account.models import School, Student, Employee
from project.models import Project
import urllib.request as urllib2
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from random import randrange

random_student_names = ["Delphia Strunk", "Aurora Kopczynski", "Estefana Chadburn", "Ora Argo", "Wai Buckman", "Bridgett Crimi", "Emilia Butters", "Louisa Lajoie", "Olene Forte", "Stephane Davisson", "Ernest Theis", "Gaynell Niel", "Kathrin Bittle", "Earl Guin", "Janise Watson", "Amado Dorr", "Leeanna Moises", "Mazie Couey", "Vernia Lucarelli",
                        "Al Fawley", "Tarra Durrant", "Kimberly Ochoa", "Napoleon Meyerson", "Jean Wilkens", "Madalene Wiedman", "Jaimie Guido", "Holley Archie", "Karren Bavaro", "Shelton Mancha", "Emma Waltman", "Jayne Beam", "Audrie Canela", "Bailey Philson", "Macie Diener", "Florida Baudoin", "Keeley Newcombe", "August Dudgeon", "Cierra Tiedemann", "Nam Baldonado"]
random_employee_names = ["Sacha Striplin", "Zulema Wisener", "Dottie Linden",
                         "May Lipsett", "Kaitlyn Hulen", "Luisa Lally", "Rolanda Provence"]
random_school_contact_names = [
    "Carole Besse", "Delana Stodola", "Matt Tarrant", "Nadene Ference"]
school_names_and_avatars = {
    "Pennsylvania State University": "http://www.logo-designer.co/wp-content/uploads/2015/08/2015-Penn-State-University-logo-design-4.png",
    "Michigan State University": "http://www.buildabear.com/ProductImages/BABW_US/XL/1700x.jpg",
    "University of Virginia": "http://www.logospike.com/wp-content/uploads/2015/04/University_Of_Virginia_Logo_01.png",
    "Purdue University": "http://vector.me/files/images/5/8/58289/purdue_university_boilermakers.png"}
school_names = list(school_names_and_avatars.keys())
project_names_and_avatars = {
    "Capstone Tracker Project": "https://s-media-cache-ak0.pinimg.com/736x/26/63/e5/2663e5cd08194d30314a3f0b7a6c32e0.jpg",
    "Green Energy SODOSOPA": "https://res.cloudinary.com/teepublic/image/private/s--Y7OuJmeQ--/t_Preview/b_rgb:ffffff,c_limit,f_jpg,h_313,q_90,w_313/v1446245008/production/designs/299463_1.jpg",
    "Robot Wall-E": "http://vignette2.wikia.nocookie.net/disney/images/8/85/Wall-e.jpg.jpg/revision/latest?cb=20140429123637",
    "Quadcopter XL": "http://www.robotshop.com/media/files/images2/550mm-rtf-quadcopter-uav-1-large.jpg"
}
project_names = list(project_names_and_avatars.keys())
brief_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sollicitudin urna odio."
description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sollicitudin urna odio, vel mattis ligula pulvinar et. Nulla urna urna, laoreet id nibh egestas, volutpat lobortis metus. Vestibulum ac velit euismod, bibendum elit a, blandit nunc. Fusce tincidunt metus justo, eleifend pretium augue ullamcorper non. Proin blandit fermentum aliquet. Vestibulum efficitur urna a mollis bibendum. Aenean rutrum interdum arcu, vitae fermentum mi efficitur in. Cras dictum, neque vitae mollis tristique, ante metus eleifend ante, et pellentesque sapien felis sit amet ante. Suspendisse eget sollicitudin est. Etiam at lacus nunc. Sed viverra interdum cursus."


def download_image(name, image, url):
    try:
        input_file = BytesIO(urllib2.urlopen(url).read())
    except urllib2.HTTPError:
        print('No image for ' + name)
    output_file = BytesIO()
    img = Image.open(input_file)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(output_file, "JPEG")
    image.save(name+".jpg", ContentFile(output_file.getvalue()), save=False)

# Populating precreated Schools
for i in range(len(school_names_and_avatars)):
    if not School.objects.filter(name=school_names[i]):
        school = School(name=school_names[i], contact_first_name=random_school_contact_names[i].split(' ')[
                        0], contact_last_name=random_school_contact_names[i].split(' ')[1], contact_email=random_school_contact_names[i]+'@gmail.com', contact_phone="+12345678900")
        school.save()
        download_image(
            school.name, school.school_avatar, school_names_and_avatars[school_names[i]])
        school.save()

print("Finished populating Schools")

# Populating precreated projects
for i in range(len(project_names_and_avatars)):
    if not Project.manager.filter(title=project_names[i]):
        project = Project(title=project_names[
                          i], brief_description=brief_description, description=description)
        project.save()
        download_image(
            project.title, project.image, project_names_and_avatars[project_names[i]])
        for tag in project.title.split(' '):
            project.tags.add(tag)
        project.save()

print("Finished populating Projects")

# Populating precreated Employees
project_list = Project.manager.all()
for employee_name in random_employee_names:
    first_name = employee_name.split(' ')[0]
    last_name = employee_name.split(' ')[1]
    if not Employee.objects.filter(first_name=first_name, last_name=last_name, email=first_name+last_name+"@gmail.com"):
        employee = Employee(first_name=first_name, last_name=last_name, email=first_name+last_name +
                            "@gmail.com", project=project_list[randrange(len(project_list))], position="Supervisor")
        employee.set_password("123")
        employee.save()
        try:
            confirmation_key = employee.confirmation_key
        except:
            confirmation_key = employee.add_unconfirmed_email(employee.email)
        employee.confirm_email(confirmation_key)

print("Finished populating Employees")

# Populating precreated Students
school_list = School.objects.all()
project_list = Project.manager.all()
for student_name in random_student_names:
    first_name = student_name.split(' ')[0]
    last_name = student_name.split(' ')[1]
    if not Student.objects.filter(first_name=first_name, last_name=last_name, email=first_name+last_name+"@gmail.com"):
        student = Student(first_name=first_name, last_name=last_name, email=first_name+last_name+"@gmail.com",
                          school=school_list[randrange(len(school_list))], project=project_list[randrange(len(project_list))])
        student.set_password("123")
        student.save()
        try:
            confirmation_key = student.confirmation_key
        except:
            confirmation_key = student.add_unconfirmed_email(student.email)
        student.confirm_email(confirmation_key)

print("Finished populating Students")
