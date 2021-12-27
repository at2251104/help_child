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

/* ----------検索ボックスによる絞り込み----------- */
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

/*--------チェックボックスによる絞り込み--------------*/
var searchBox = '.search-box'; // 絞り込む項目を選択するエリア
var listItem = '.list_item';   // 絞り込み対象のアイテム
var hideClass = 'is-hide';     // 絞り込み対象外の場合に付与されるclass名

$(function () {
    // 絞り込み項目を変更した時
    $(document).on('change', searchBox + ' input', function () {
        search_filter();
    });
});

/**
 * リストの絞り込みを行う
 */
function search_filter() {
    // 非表示状態を解除
    $(listItem).removeClass(hideClass);
    for (var i = 0; i < $(searchBox).length; i++) {
        var name = $(searchBox).eq(i).find('input').attr('name');
        // 選択されている項目を取得
        var searchData = get_selected_input_items(name);
        // 選択されている項目がない、またはALLを選択している場合は飛ばす
        if (searchData.length === 0 || searchData[0] === '') {
            continue;
        }
        // リスト内の各アイテムをチェック
        for (var j = 0; j < $(listItem).length; j++) {
            // アイテムに設定している項目を取得
            var itemData = $(listItem).eq(j).data(name);
            // 絞り込み対象かどうかを調べる
            if (searchData.indexOf(itemData) === -1) {
                $(listItem).eq(j).addClass(hideClass);
            }
        }
    }
}

/**
 * inputで選択されている値の一覧を取得する
 * @param  {String} name 対象にするinputのname属性の値
 * @return {Array}       選択されているinputのvalue属性の値
 */
function get_selected_input_items(name) {
    var searchData = [];
    $('[name=' + name + ']:checked').each(function () {
        searchData.push($(this).val());
    });
    return searchData;
}

//document.getElementById

/*document.querySelector('#switch1').addEventListener('click', function(){
   document.querySelector('.menu').classList.toggle('is-active');
});*/