$(document).ready(function () {
    // icon을 클릭한 것이 아니라면 드롭다운을 닫아준다
    $(window).on('click', function (event) {
        let allDropdowns = document.getElementsByClassName("dropdown-content")
        let targetDropdown = $(event.target).next('.dropdown-content')[0]
        // map 함수를 이용하기 위해 Array로 치환한다
        let dropdownArr = [...allDropdowns]

        // 클릭한게 icon이 아닌 경우 window를 클릭한 것이다.
        if (!event.target.matches('i')) {
            // show가 있는 div를 닫아준다
            dropdownArr.map(d => {
                if (d.classList.contains('show')) d.classList.remove('show')
            })
        } else {
            //클릭한게 icon인 경우
            if (targetDropdown.classList.contains('show')) {
                // 만일 클릭한 icon으로부터 가장 가까운 dropdown-content가 열려있으면 단순히 닫아준다.
                targetDropdown.classList.remove('show')
            } else {
                // 만일 클릭한 icon으로부터 가장 가까운 dropdown-content가 닫혀있으면 일단 모든 dropdown을 닫아준다.
                dropdownArr.map(d => d.classList.remove('show'))
                // 그 후 클릭한 icon으로부터 가장 가까운 dropdown-content를 열어준다.
                targetDropdown.classList.toggle('show')
            }
        }
    })
})