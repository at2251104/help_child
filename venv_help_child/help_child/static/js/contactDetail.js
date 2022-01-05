$(function () {
    $("#target").datepicker({
      changeYear: true,    // 年を表示
      changeMonth: true,   // 月を選択
      // ↓の日付をいじります（過去も見る必要があるため）
      minDate: '-3y +6m', // 前日以前は選択不可
      maxDate: '+3y +6m',  // 1年半後まで選択可
      buttonImage: "/static/images/calender2.png",        // カレンダーアイコン画像
      buttonText: "カレンダーから選択", // ツールチップ表示文言
      buttonImageOnly: true,           // 画像として表示
      showOn: "both",
    });
    $("#from1").datepicker({
      changeYear: true,    // 年を表示
      changeMonth: true,   // 月を選択
      // ↓の日付をいじります（過去も見る必要があるため）
      minDate: '-3y +6m', // 前日以前は選択不可
      maxDate: '+3y +6m',  // 1年半後まで選択可
      buttonImage: "/static/images/calender2.png",        // カレンダーアイコン画像
      buttonText: "カレンダーから選択", // ツールチップ表示文言
      buttonImageOnly: true,           // 画像として表示
      showOn: "both",
    });
    $("#to1").datepicker({
      changeYear: true,    // 年を表示
      changeMonth: true,   // 月を選択
      // ↓の日付をいじります（過去も見る必要があるため）
      minDate: '-3y +6m', // 前日以前は選択不可
      maxDate: '+3y +6m',  // 1年半後まで選択可
      buttonImage: "/static/images/calender2.png",        // カレンダーアイコン画像
      buttonText: "カレンダーから選択", // ツールチップ表示文言
      buttonImageOnly: true,           // 画像として表示
      showOn: "both",
    });
    var OBJ = $("target");
    OBJ.position = absolute;
    //var plc = $("target").position();
    //console.log(plc);
  });
  
  
  
  // $(function() {
  //   var from1 = $("#from1").datepicker({
  //         onSelect: function(selectedDate) {
  //           $("#to1").datepicker("option","minDate",selectedDate);
  //         }
  //     });
  //   var to1 = $("#to1").datepicker({
  //           onSelect: function(selectedDate ) {
  //           $("#from1").datepicker("option","maxDate",selectedDate);
  //         }
  //     });
  // });