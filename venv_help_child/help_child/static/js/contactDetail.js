const week = ["日", "月", "火", "水", "木", "金", "土"];
const today = new Date();
// 月末だとずれる可能性があるため、1日固定で取得
var showDate = new Date(today.getFullYear(), today.getMonth(), today.getDay());

// 初期表示
window.onload = function () {
    showProcess(today, calendar);
};

// カレンダー内の各要素にリンクを設定、Detailに飛べるようにする
function OnLinkClick(year,month,count){
    var n = year * 10000; // YYYY0000
	n += month * 100 + 100; // YYYYMM00
	n += count; // YYYYMMDD

    return n;
}

// 前の日表示
function prev(){
    showDate.setMonth(showDate.getDay() - 1);
    showProcess(showDate);
}

// 次の日表示
function next(){
    showDate.setMonth(showDate.getDay() + 1);
    showProcess(showDate);
}