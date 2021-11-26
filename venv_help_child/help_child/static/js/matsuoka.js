$(function () {
    // 「すべてを選択」changeイベント
    $('.js-check-all').on('change', function (event) {
        // data-check-allで対象グループを取得
        var group = $(event.target).data('check-all');
        // data-check-all="hobby" の形式に直す
        var dataCheckGroup = '[data-check-all="' + group + '"]';

        // 「すべてを選択」がチェックされているとき
        if ($(event.target).prop('checked')) {
            // 同じ対象内のチェックボックスをすべてチェックする (disabledを除く)
            $('.js-check-all-target')
                .filter(dataCheckGroup)
                .find('input[type="checkbox"]:not(:disabled)')
                .prop('checked', true);

            return;
        }

        // 「すべてを選択」がチェックされていないとき
        // 同じ対象内のチェックボックスをすべてチェックを外す (disabledを除く)
        $('.js-check-all-target')
            .filter(dataCheckGroup)
            .find('input[type="checkbox"]:not(:disabled)')
            .prop('checked', false);
    });
});

/* ----------絞り込み検索----------- */
function myFunction() {
    // Declare variables
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById('search-text');
    filter = input.value.toUpperCase();
    ul = document.getElementById("list");
    li = ul.getElementsByTagName('li');

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}