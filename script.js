function showSection(sectionId) {
    let sections = document.querySelectorAll(".cars-section");
    sections.forEach(section => section.style.display = "none");
    document.getElementById(sectionId).style.display = "block";
}

function toggleInfo(id) {
    let info = document.getElementById(id);
    if (info.style.display === "none" || info.style.display === "") {
        info.style.display = "block";
        setTimeout(() => {
            info.style.opacity = "1";
        }, 10);
    } else {
        info.style.opacity = "0";
        setTimeout(() => {
            info.style.display = "none";
        }, 500);
    }
}

/* Дополнительный эффект на кнопках */
document.querySelectorAll(".button").forEach(button => {
    button.addEventListener("mouseover", () => {
        button.style.transform = "scale(1.1)";
    });
    button.addEventListener("mouseout", () => {
        button.style.transform = "scale(1)";
    });
});
function addCar() {
    const nameInput = document.getElementById("carName");
    const descInput = document.getElementById("carDescription");
    const fileInput = document.getElementById("carImage");
    const carList = document.getElementById("carList");

    if (!nameInput.value || !descInput.value || !fileInput.files[0]) {
        alert("Введите название, описание и выберите картинку!");
        return;
    }

    // Создаем контейнер для машинки
    const carBlock = document.createElement("div");
    carBlock.classList.add("car");

    // Создаем контейнер для информации (справа от картинки)
    const infoBlock = document.createElement("div");
    infoBlock.classList.add("car-info");

    const carTitle = document.createElement("h3");
    carTitle.textContent = nameInput.value;

    const carDesc = document.createElement("p");
    carDesc.textContent = descInput.value;

    // Создаем и загружаем изображение
    const reader = new FileReader();
    reader.onload = function(event) {
        const img = document.createElement("img");
        img.src = event.target.result;
        img.classList.add("car-image");

        // Добавляем в блоки контент
        infoBlock.appendChild(carTitle);
        infoBlock.appendChild(carDesc);
        carBlock.appendChild(img); // Картинка слева
        carBlock.appendChild(infoBlock); // Информация справа
        carList.appendChild(carBlock);
    };
    reader.readAsDataURL(fileInput.files[0]);

    // Очищаем поля после добавления
    nameInput.value = "";
    descInput.value = "";
    fileInput.value = "";
}
