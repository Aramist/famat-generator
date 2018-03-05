var questionBody = "";
var answerChoices = ["", "", "", "", ""];

var updateMath = function(){
    MathJax.Hub.Queue(
        ["Typeset", MathJax.Hub, "question-body-display"],
        ["Typeset", MathJax.Hub, "a-display"],
        ["Typeset", MathJax.Hub, "b-display"],
        ["Typeset", MathJax.Hub, "c-display"],
        ["Typeset", MathJax.Hub, "d-display"],
        ["Typeset", MathJax.Hub, "e-display"]);
};

$("#question-body").keyup(function(){
    questionBody = $("#question-body").val();
    $("#question-body-display").html(questionBody);
    updateMath();
});

$("#answer-choice-a").keyup(function(){
    answerChoices[0] = $("#answer-choice-a").val();
    $("#a-display").html(answerChoices[0]);
    updateMath();
});
$("#answer-choice-b").keyup(function(){
    answerChoices[1] = $("#answer-choice-b").val();
    $("#b-display").html(answerChoices[1]);
    updateMath();
});
$("#answer-choice-c").keyup(function(){
    answerChoices[2] = $("#answer-choice-c").val();
    $("#c-display").html(answerChoices[2]);
    updateMath();
});
$("#answer-choice-d").keyup(function(){
    answerChoices[3] = $("#answer-choice-d").val();
    $("#d-display").html(answerChoices[3]);
    updateMath();
});
$("#answer-choice-e").keyup(function(){
    answerChoices[4] = $("#answer-choice-e").val();
    $("#e-display").html(answerChoices[4]);
    updateMath();
});