﻿
       function updateParams(days) {
           param_text = "byweekday:";
           for (i=0;i < days.length; i++){
               //console.log(days[i])
               if (i > 0) {
                   param_text = param_text + ','
               }
               param_text = param_text + days[i]
              
           }
           param_text = param_text + ';'
           console.log(param_text)
           $('#id_params').val(param_text);

       }
$(".checkbox").change(function () {
    var days=[]
    //console.log("changed")
    $(".checkbox").each(function () {
        if (this.checked) {
            //console.log(this);
            days.push(this.value);
        }
    })
    if (days.length > 0) {
        //console.log("We have days we should set param")
    }
    updateParams(days);
    //console.log(days);
       
});
