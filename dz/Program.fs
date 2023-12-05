// Использование List.filter и оператора |> для создания нового списка evenSquaredNumbers
let numbers = [1; 2; 3; 4; 5; 6; 7; 8; 9; 10]

let evenSquaredNumbers =
    numbers
    |> List.filter (fun x -> x % 2 = 0)
    |> List.map (fun x -> x * x)

printfn "%A" evenSquaredNumbers