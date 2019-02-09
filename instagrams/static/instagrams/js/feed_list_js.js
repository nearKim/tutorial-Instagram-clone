$(document).ready(function () {
    $(window).on('click', function (event) {
        // 0. 공통 변수 초기화
        let target = $(event.target)

        // 1. Dropdown 관련 로직
        let allDropdowns = document.getElementsByClassName("dropdown-content")
        let targetDropdown = target.next('.dropdown-content')[0]
        // map 함수를 이용하기 위해 Array로 치환한다
        let dropdownArr = [...allDropdowns]

        // 클릭한게 icon이 아닌 경우 window를 클릭한 것이다.
        if (!event.target.matches('i')) {
            // show가 있는 div를 닫아준다
            dropdownArr.map(d => {
                if (d.classList.contains('show')) d.classList.remove('show')
            })
        } else if (target.hasClass('fa-ellipsis-v"')) {
            //클릭한게 더보기 icon인 경우
            if (targetDropdown.classList.contains('show')) {
                // 만일 클릭한 icon으로부터 가장 가까운 dropdown-content가 열려있으면 단순히 닫아준다.
                targetDropdown.classList.remove('show')
            } else {
                // 만일 클릭한 icon으로부터 가장 가까운 dropdown-content가 닫혀있으면 일단 모든 dropdown을 닫아준다.
                dropdownArr.map(d => d.classList.remove('show'))
                // 그 후 클릭한 icon으로부터 가장 가까운 dropdown-content를 열어준다.
                targetDropdown.classList.toggle('show')
            }
        } else if (target.hasClass('fa-comment')) {
            // 1. 말풍선 기준으로 가장 가까운 .button-container div를 찾는다.
            // 2. 그것과 동일한 위치의 .comment-creator-div div를 찾는다.
            // 3. 하위 요소를 순회하며 textarea 를 찾으면 그것이 포커싱하고자하는 댓글창이다
            target.closest('.button-container')
                .siblings('.comment-creator-div')
                .find('textarea')[0]
                .focus()
        }
    })
})