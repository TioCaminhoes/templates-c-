// Exercicio: pilha, fila e lista com dois parametros genericos (T e U)
// Parte 1: nossas classes
// Parte 2: exemplos do PDF (stack, queue, list) para comparar
#include <iostream>
#include <stack>
#include <queue>
#include <list>
using namespace std;

#define MAX 100

// ====================== PARTE 1: NOSSAS CLASSES ======================

template <class T, class U>
class Pilha {
    T a[MAX];
    U b[MAX];
    int topo;
public:
    Pilha() { topo = -1; }
    bool vazia() { return topo == -1; }
    void push(T x, U y) {
        if (topo == MAX - 1) {
            cout << "Pilha cheia!" << endl;
            return;
        }
        topo++;
        a[topo] = x;
        b[topo] = y;
    }
    void pop() {
        if (vazia()) {
            cout << "Pilha vazia!" << endl;
            return;
        }
        topo--;
    }
    T topoT() { return a[topo]; }
    U topoU() { return b[topo]; }
};

template <class T, class U>
class Fila {
    T a[MAX];
    U b[MAX];
    int inicio, fim, qtd;
public:
    Fila() { inicio = 0; fim = 0; qtd = 0; }
    bool vazia() { return qtd == 0; }
    void push(T x, U y) {
        if (qtd == MAX) {
            cout << "Fila cheia!" << endl;
            return;
        }
        a[fim] = x;
        b[fim] = y;
        fim = (fim + 1) % MAX;
        qtd++;
    }
    void pop() {
        if (vazia()) {
            cout << "Fila vazia!" << endl;
            return;
        }
        inicio = (inicio + 1) % MAX;
        qtd--;
    }
    T frenteT() { return a[inicio]; }
    U frenteU() { return b[inicio]; }
};

template <class T, class U>
class Lista {
    T a[MAX];
    U b[MAX];
    int qtd;
public:
    Lista() { qtd = 0; }
    int tamanho() { return qtd; }
    void inserir(int pos, T x, U y) {
        if (qtd == MAX || pos < 0 || pos > qtd) {
            cout << "Nao foi possivel inserir!" << endl;
            return;
        }
        for (int i = qtd; i > pos; i--) {
            a[i] = a[i - 1];
            b[i] = b[i - 1];
        }
        a[pos] = x;
        b[pos] = y;
        qtd++;
    }
    void remover(int pos) {
        if (pos < 0 || pos >= qtd) {
            cout << "Posicao invalida!" << endl;
            return;
        }
        for (int i = pos; i < qtd - 1; i++) {
            a[i] = a[i + 1];
            b[i] = b[i + 1];
        }
        qtd--;
    }
    void mostrar() {
        for (int i = 0; i < qtd; i++)
            cout << "(" << a[i] << ", " << b[i] << ") ";
        cout << endl;
    }
};

// Testes nossos (fazem a mesma coisa dos exemplos do PDF)

void minha_pilha()
{
    Pilha<int, int> mystack;

    for (int i = 0; i < 5; ++i) mystack.push(i, i * 10);

    cout << "Popping out elements...";
    while (!mystack.vazia())
    {
        cout << ' ' << mystack.topoT();
        mystack.pop();
    }
    cout << '\n';
}

void minha_fila()
{
    Fila<int, int> myqueue;
    int myint;
    int pos = 0;

    cout << "Please enter some integers (enter 0 to end):\n";

    do {
        cin >> myint;
        myqueue.push(myint, pos);
        pos++;
    } while (myint);

    cout << "myqueue contains: ";
    while (!myqueue.vazia())
    {
        cout << ' ' << myqueue.frenteT();
        myqueue.pop();
    }
    cout << '\n';
}

void minha_lista()
{
    Lista<int, int> mylist;
    int myint;

    cout << "Please enter some integers (enter 0 to end):\n";

    do {
        cin >> myint;
        mylist.inserir(mylist.tamanho(), myint, 0);   // insere no fim
    } while (myint);

    cout << "mylist stores " << mylist.tamanho() << " numbers.\n";
}

// ====================== PARTE 2: CODIGOS DO PDF ======================
// (o corpo e igual ao do slide; so troquei "main" por um nome de funcao)

// list::push_back
void lista_pdf ()
{
  std::list<int> mylist;
  int myint;

  std::cout << "Please enter some integers (enter 0 to end):\n";

  do {
    std::cin >> myint;
    mylist.push_back (myint);
  } while (myint);

  std::cout << "mylist stores " << mylist.size() << " numbers.\n";
}

// stack::push/pop
void pilha_pdf ()
{
  std::stack<int> mystack;

  for (int i=0; i<5; ++i) mystack.push(i);

  std::cout << "Popping out elements...";
  while (!mystack.empty())
  {
     std::cout << ' ' << mystack.top();
     mystack.pop();
  }
  std::cout << '\n';
}

// queue::push/pop
void fila_pdf ()
{
  std::queue<int> myqueue;
  int myint;

  std::cout << "Please enter some integers (enter 0 to end):\n";

  do {
    std::cin >> myint;
    myqueue.push (myint);
  } while (myint);

  std::cout << "myqueue contains: ";
  while (!myqueue.empty())
  {
    std::cout << ' ' << myqueue.front();
    myqueue.pop();
  }
  std::cout << '\n';
}

// ====================== MENU ======================

int main() {
    int op;
    do {
        cout << "\n===== MENU =====" << endl;
        cout << "1 - Nossa pilha" << endl;
        cout << "2 - stack do PDF" << endl;
        cout << "3 - Nossa fila" << endl;
        cout << "4 - queue do PDF" << endl;
        cout << "5 - Nossa lista" << endl;
        cout << "6 - list do PDF" << endl;
        cout << "0 - Sair" << endl;
        cout << "Opcao: ";
        cin >> op;

        if (op == 1) minha_pilha();
        else if (op == 2) pilha_pdf();
        else if (op == 3) minha_fila();
        else if (op == 4) fila_pdf();
        else if (op == 5) minha_lista();
        else if (op == 6) lista_pdf();
    } while (op != 0);

    return 0;
}