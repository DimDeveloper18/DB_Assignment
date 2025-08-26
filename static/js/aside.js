// Aside JavaScript code

const martic2 = document.getElementById("martic");
const asideHead = document.getElementById("asHead");
const sale1 = document.getElementById("battery");
const sale2 = document.getElementById("drill");
const sale3 = document.getElementById("skillsaw");
const sale4 = document.getElementById("cordlessdrill");
const sale1Wind = document.getElementById("windDet1");

                            // Changing color by mouseover the aside head

asideHead.addEventListener("mouseover", () => {
    asideHead.classList.add("highlight");
});
asideHead.addEventListener("mouseout", () => {
    asideHead.classList.remove("highlight");
});

                           // Changing color to Sale item 1

sale1.addEventListener("mouseover", () => {
    sale1.classList.add("highlight");
});
sale1.addEventListener("mouseout", () => {
    sale1.classList.remove("highlight");
});

document.getElementById("battery").addEventListener("click", (e)=>{
    if( !e.currentTarget.classList.contains("clicked") ){
        e.currentTarget.classList.add("clicked");
    }else{
        e.currentTarget.classList.remove("clicked");
    }
    if( e.currentTarget.classList.contains("clicked") ){
           e.currentTarget.lastElementChild.style.display="block";
    }else{
        e.currentTarget.lastElementChild.style.display="none";
    }
});

                            // Changing color to Sale item 2

sale2.addEventListener("mouseover", () => {
    sale2.classList.add("highlight");
});
sale2.addEventListener("mouseout", () => {
    sale2.classList.remove("highlight");
});

document.getElementById("drill").addEventListener("click", (e)=>{
    if( !e.currentTarget.classList.contains("clicked") ){
        e.currentTarget.classList.add("clicked");
    }else{
        e.currentTarget.classList.remove("clicked");
    }
    if( e.currentTarget.classList.contains("clicked") ){
           e.currentTarget.lastElementChild.style.display="block";
    }else{
        e.currentTarget.lastElementChild.style.display="none";
    }
});

                            // Changing color to Sale item 3

sale3.addEventListener("mouseover", () => {
    sale3.classList.add("highlight");
});
sale3.addEventListener("mouseout", () => {
    sale3.classList.remove("highlight");
});

document.getElementById("skillsaw").addEventListener("click", (e)=>{
    if( !e.currentTarget.classList.contains("clicked") ){
        e.currentTarget.classList.add("clicked");
    }else{
        e.currentTarget.classList.remove("clicked");
    }
    if( e.currentTarget.classList.contains("clicked") ){
           e.currentTarget.lastElementChild.style.display="block";
    }else{
        e.currentTarget.lastElementChild.style.display="none";
    }
});

                            // Changing color to Sale item 4

sale4.addEventListener("mouseover", () => {
    sale4.classList.add("highlight");
});
sale4.addEventListener("mouseout", () => {
    sale4.classList.remove("highlight");
});

document.getElementById("cordlessdrill").addEventListener("click", (e)=>{
    if( !e.currentTarget.classList.contains("clicked") ){
        e.currentTarget.classList.add("clicked");
    }else{
        e.currentTarget.classList.remove("clicked");
    }
    if( e.currentTarget.classList.contains("clicked") ){
           e.currentTarget.lastElementChild.style.display="block";
    }else{
        e.currentTarget.lastElementChild.style.display="none";
    }
});