const tabs = document.querySelectorAll(".tab");
const forms = document.querySelectorAll(".form-div");

const removeActiveTab = () => {
  tabs.forEach(tab => tab.classList.remove("active"));
};

const removeActiveForm = () => {
  forms.forEach(form => form.classList.remove("current"));
};

function setActiveForm(tab) {
  removeActiveForm();

  forms.forEach(form => {
    if (tab.classList.contains(form.dataset['form'].toLowerCase())) {
      form.classList.add('current')
    }
  });
}


function setActiveTab(tab) {
  if (!tab.classList.contains("active")) {
    removeActiveTab();
    tab.classList.add("active");
  }
}


tabs.forEach(tab => {
  tab.addEventListener("click", () => {
    debugger;
    setActiveTab(tab);
    setActiveForm(tab);
  });
});