const djangoForms = document.getElementsByClassName("django-form");

if (djangoForms){
    Array.from(djangoForms).map((form) => {
        Array.form(form).map((element) => {
            switch (element.tagName.toLowerCase()) {
                case "input":
                    element.classList.add("form-control");
                    break;
                case "textarea":
                    element.classList.add("form-control")
                    break;
                default:
                    console.log(element);
                    break;
              }

        });
    });
}