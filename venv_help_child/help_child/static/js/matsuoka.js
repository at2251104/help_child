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
$(function () {
    searchWord = function () {
        var searchResult,
            searchText = $(this).val(), // 検索ボックスに入力された値
            targetText,
            hitNum;

        // 検索結果を格納するための配列を用意
        searchResult = [];

        // 検索結果エリアの表示を空にする
        $('#search-result__list').empty();
        $('.search-result__hit-num').empty();

        // 検索ボックスに値が入ってる場合
        if (searchText != '') {
            $('.target-area li').each(function () {
                targetText = $(this).text();

                // 検索対象となるリストに入力された文字列が存在するかどうかを判断
                if (targetText.indexOf(searchText) != -1) {
                    // 存在する場合はそのリストのテキストを用意した配列に格納
                    searchResult.push(targetText);
                }
            });

            // 検索結果をページに出力
            for (var i = 0; i < searchResult.length; i++) {
                $('<span>').text(searchResult[i]).appendTo('#search-result__list');
            }

            // ヒットの件数をページに出力
            hitNum = '<span>検索結果</span>：' + searchResult.length + '件見つかりました。';
            $('.search-result__hit-num').append(hitNum);
        }
    };

    // searchWordの実行
    $('#search-text').on('input', searchWord);
});

$(function () {
    searchWord = function () {
        var searchText = $(this).val(), // 検索ボックスに入力された値
            targetText;

        $('.target-area li').each(function () {
            targetText = $(this).text();

            // 検索対象となるリストに入力された文字列が存在するかどうかを判断
            if (targetText.indexOf(searchText) != -1) {
                $(this).removeClass('hidden');
            } else {
                $(this).addClass('hidden');
            }
        });
    };

    // searchWordの実行
    $('#search-text').on('input', searchWord);
});

/* 絞り込み機能-part2 */

function myFunction() {
    // Declare variables
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
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