// const itemId = document.getElementById("itemNum");

function createCheckbox(){
    const checkBox = document.createElement("input");
    checkBox.classList.add("selectBox");
    checkBox.setAttribute("type", "checkbox");
    checkBox.addEventListener("click", function(){
        toggleItemAdded()
    })
}

// Highlights the line of the table by click on it

const itemLine = document.querySelector(".lightItem");
itemLine.addEventListener("click", function(event){
    const clickedRow = event.target.closest("tr");

    if (clickedRow && itemLine.contains(itemLine)){
        clickedRow.classList.tooggle("rowprod");
    }
});
