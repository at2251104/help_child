const week = ["日", "月", "火", "水", "木", "金", "土"];
const today = new Date();


var showDate = new Date(today.getFullYear(), today.getMonth(), today.getDay());


// 前の日付表示
function prev(){
    showDate.setMonth(showDate.getDay() - 1);
    showProcess(showDate);
}

// 次の日付表示
function next(){
    showDate.setMonth(showDate.getDay() + 1);
    showProcess(showDate);
}