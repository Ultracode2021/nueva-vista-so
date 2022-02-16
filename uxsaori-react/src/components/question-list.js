import React, {useState, useEffect} from 'react';

function QuestionList() {

  const [ questions, setQuestions ] = useState(null);
  const [ loading, setLoading ] = useState(false);
  const [ error, setError ] = useState(false);

  useEffect(()=>{
    setLoading(true);
    const getData = async() => {
      await fetch('http://127.0.0.1:8000/polls/questions')
      .then(resp => resp.json())
      .then( data => {
        setQuestions(data);
        setLoading(false);
      }).catch( e =>{
        setError(true);
        setLoading(false);
      })
    }
    getData();
  },[])

  if (error) return <h1> Error </h1>
  if (loading) return <h1> Loading </h1>

  return (
    <div>
        { questions && questions.map(question=>{
          return <p key = {question.id}> {question.text}{question.choice_text} </p>
        })}
    </div>
  );
}

export default QuestionList;
