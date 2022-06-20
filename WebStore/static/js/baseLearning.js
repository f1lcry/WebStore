console.log("Hello!!!");
        function pause() {
            alert("Hello world!");
        };
<!--        setTimeout(pause, 3000);-->
        var s = Math.random() * 1000;

<!--        if (s <= 400) {-->
<!--            alert("smaller");-->
<!--        }-->
<!--        else {-->
<!--            alert("bigger: " + s)-->
<!--        };-->

<!--        alert(1 / 0);-->
<!--        alert("a" * 2);-->
<!--        alert(typeof(s));-->
        var a = 456;
        var ch = 460;
        a ++
       var evening = "evening"

       switch (evening) {
            case "night":
                alert("Good night!");
                break;
            case "evening":
                alert("Good evening!");
                break;
            default:
                alert("Good day!");
       }

<!--       for (d = 1; s; d ++) {-->
<!--            if (d > 10) {-->
<!--                break;-->
<!--            }-->
<!--            alert(d);-->
<!--       }-->

<!--       do {-->
<!--            console.log(a ++)-->
<!--       }-->
<!--       while (a >= ch)-->

    var spisok = [12, 124, 967, "43"];
    var spisokTwo = new Array(12, 124, 967, "43");
    spisokTwo.push("element", 456);
    delete spisok[3]
    console.log(spisok, spisokTwo);

    console.log("")
    console.log("")
    console.log("")



<!--                OBJECTS             -->
    var car = {
        owner: "company's name",
        price: 12345,
        color: "white",
        startEngine: function () {
            return "vrrrrrr";
        }
    };
    console.log(car.color);
    car.year = 2015
    console.log(car)
    delete car.price
    console.log(car)
    console.log(car.startEngine())



<!--         DOM             -->
<!--    document.getElementById("Smartphones")-->
<!--    document.getElementById("Smartphones").innerHTML = "text"-->

    function Breaker () {
        var smartphone = document.getElementById("Smartphones");
        smartphone.innerHTML = "text";
    };
    Window.onload = setTimeout(Breaker, 1);
    var number = prompt("")