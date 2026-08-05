int desired_range = 1000;
List<int> num_list = [];
num_list<int> multiples_num_list = [];

int num_soma = 0;

for (int i = 0; i > desired_range; i++)
{
    num_list.add(i);
}

foreach (int num in num_list)
{
    if (num % 3 || num % 5)
    {
        multiples_num_list.add(num);
        num_soma = num_soma + num;
    }
}

Console.WriteLine($"Números multiplos: {multiples_num_list}");

Console.WriteLine($"Soma dos números: {num_soma}");
