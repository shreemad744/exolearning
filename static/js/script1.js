const Questions = [];
const TotalQuestions = 10;

const fetchQuestions = async function() {
    try {
        const response = await fetch('/api/questions1');
        if (!response.ok) {
            throw new Error("Error in Network Response: " + response.statusText);
        }
        let data = await response.json();
        for (let i = 0; i < TotalQuestions; i++) {
            let randomNumber = Math.floor(Math.random() * data.length);

            let temp = {
                "question": data[randomNumber]["question_text"],
                "answers": [
                    {text: data[randomNumber]["options"][0], correct: (data[randomNumber]["options"][0] === data[randomNumber]["correct_answer"])},
                    {text: data[randomNumber]["options"][1], correct: (data[randomNumber]["options"][1] === data[randomNumber]["correct_answer"])},
                    {text: data[randomNumber]["options"][2], correct: (data[randomNumber]["options"][2] === data[randomNumber]["correct_answer"])},
                    {text: data[randomNumber]["options"][3], correct: (data[randomNumber]["options"][3] === data[randomNumber]["correct_answer"])}
                ]
            };
            data.splice(randomNumber,1)
            Questions.push(temp);
        }


    } catch (error) {
        console.error("Problem with fetching questions: ", error);
    }
};



const QuestionElement = document.getElementById("question");
const AnswerButton = document.getElementById("answer-buttons");
const next = document.getElementById("next-btn");
const info_button = document.getElementById("info-btn")
const title_button = document.getElementById("question")


let CurrentQuestionIndex = 0;
let Score = 0;

function StartQuiz(){
    CurrentQuestionIndex = 0;
    Score = 0;
    next.innerHTML = "Check"
    ShowQuestion()
}

function ShowQuestion() {
    ResetState()
    let CurrentQuestion = Questions[CurrentQuestionIndex];
    let QuestionNo= CurrentQuestionIndex + 1;
    QuestionElement.innerHTML = QuestionNo + "." + CurrentQuestion.question
    info_button.innerHTML = "Question " + QuestionNo + " of " + TotalQuestions
    CurrentQuestion.answers.forEach(answer => {
        const button = document.createElement("button");
        button.innerHTML = answer.text;
        button.classList.add("btn")
        AnswerButton.appendChild(button)
        if(answer.correct){ 
            button.dataset.correct = answer.correct;
        }
        button.addEventListener("click",ChoseAnswer);
       
    });
    next.addEventListener("click",selectAnswer)
    
}

function ResetState(){
    next.style.display = "none";
    while (AnswerButton.firstChild){
        AnswerButton.removeChild(AnswerButton.firstChild);
    }
}

function ChoseAnswer(e){
    next.style.display = "block";
    const selectedBtn = e.target;
    Array.from(AnswerButton.children).forEach(child => {
        if (child.classList.contains("chosen")){
            child.classList.remove("chosen")
        }
    });
    selectedBtn.classList.add("chosen")

}


function selectAnswer(e){
    const selectedBtn = e.target;
    if (CurrentQuestionIndex === (TotalQuestions-1)){
         selectedBtn.innerHTML = "View Score"
    }else{
         selectedBtn.innerHTML = "Check"
    }
   
    const IsCorrect = selectedBtn.dataset.correct === "true"
    Array.from(AnswerButton.children).forEach(child => {
        if (child.classList.contains("chosen")){
            if (child.dataset.correct){
                child.classList.add("correct")
                Score++;
            }else{
                child.classList.add("incorrect")
                Array.from(AnswerButton.children).forEach(child => {
                    if (child.dataset.correct){
                        child.classList.add("correct")
                    }
                });
            }
            child.classList.remove("chosen")
        }
        child.disabled = true; 
    });
    next.removeEventListener("click",selectAnswer)

    if (CurrentQuestionIndex <= (TotalQuestions-1)){
        next.addEventListener("click", NextQuestion)
    }
    
}

function NextQuestion(){
    CurrentQuestionIndex++;
    next.removeEventListener("click", NextQuestion)
    if (CurrentQuestionIndex <= (TotalQuestions-1)){
        ShowQuestion()
    }else{
        title_button.innerHTML = "Your Score"
        title_button.classList.add("center")
        while (AnswerButton.firstChild){
            AnswerButton.removeChild(AnswerButton.firstChild);
        }
        info_button.style.display = "None";
        next.style.float = "None";
        const Text = document.createElement("h3");
        AnswerButton.appendChild(Text)
        Text.textContent = Score + " out of " + TotalQuestions + " Questions"
        Text.style.textAlign = "Center"
        Text.style.fontSize = "35px";
        next.innerHTML = "Check Out Your Personalized Content"
        next.style.width = "325px"

        next.addEventListener("click",function(){
            window.location.href = "/reels"
        })

    }
}


(async () => {
    await fetchQuestions(); 
    StartQuiz()
})();

window.addEventListener('beforeunload', function (e) {
    e.preventDefault(); 
    e.beforeunload = ''; 
    return ''; 
});



    