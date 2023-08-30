{
    "role": "user",
    "content": "Given the following possible annotations: \n
    ```json\n" + definitions + "\n```
    Select the index for the most fitting description for the
    identifier <| " + match_variable + " |> from the following
    text." 
    + possible_affixes + 
    "\n Only return the value of 
    the index and nothing else. Do not add any explanation 
    otherwise the API breaks. 
    The identifier has been marked 
    with <||>. 
    The text is as follows: ```txt\n"
    + context +
    "\n```"
}