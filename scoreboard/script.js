let guestcount = document.getElementById("guest")
let homecount = document.getElementById("home")
let home = 0
let guest = 0

function high(){
    if (Number(guestcount.innerText) > Number(homecount.innerText)) {
        guestcount.style.color = "red"
        homecount.style.color = "green"
        console.log("You are eligible to vote.")
    } else if(Number(guestcount.innerText) < Number(homecount.innerText)) {
        homecount.style.color = "red"
        guestcount.style.color = "green"
    }
    
}

function oneplus(){
    home += 1
    console.log(home)
    console.log(homecount)
    homecount.innerText = home
    high()
}

function twoplus(){
    home += 2
    console.log(home)
    console.log(homecount)
    homecount.innerText = home
    high()
}

function threeplus(){
    home += 3
    console.log(home)
    console.log(homecount)
    homecount.innerText = home
    high()
}

function oneplusg(){
    guest += 1
    console.log(guest)
    console.log(guestcount)
    guestcount.innerText = guest
    high()
}

function twoplusg(){
    guest += 2
    console.log(guest)
    console.log(guestcount)
    guestcount.innerText = guest
    high()
}

function threeplusg(){
    guest += 3
    console.log(guest)
    console.log(guestcount)
    guestcount.innerText = guest
    high()

}

function newgame(){
    guest = 0
    home = 0
    guestcount.innerText = guest
    homecount.innerText = home
    homecount.style.color = "yellow"
    guestcount.style.color = "yellow"
}