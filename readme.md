<p align="center">
 <img width="150px" src="autopy-downloader.ico" align="center" alt="AutoPy Downloader Icon"/>
 <h1 align="center">AutoPy Downloader</h1>
 <p align="center">Arquivo <strong>python</strong> utilizado para automatizar algumas tarefas no navegador.</p>
</p>

<p align="center">
    <a href="https://github.com/ylJeferson/autopy-downloader">Download</a>
    ·
    <a href="https://github.com/ylJeferson/autopy-downloader/issues/new/choose">Reportar Bug</a>
    ·
    <a href="https://github.com/ylJeferson/autopy-downloader/issues/new/choose">Sugerir Ideias</a>
  </p>
<p align="center">Gostou do projeto? Por favor, considere realizar uma <a href="https://www.paypal.com/donate/?business=3G3JKT9E3ZKXU&no_recurring=0&item_name=Muito+obrigado%2C+com+este+apoio+pretendo+crescer+cada+vez+mais%21&currency_code=BRL">doação</a> para me ajudar!

## Modo de usar

`python "autopy-downloader.py" -s url -x "xpath1,xpath2,xpath3" -i "False"` <br>
 - `-i` Execução dos comandos em segundo plano. _Padrão: True - Navegador em segundo plano_
 - `-s` Url do site que se deseja acessar.
 - `-x` xpath do elemento que você deseja clicar.
 
<details>
  <summary>Exemplo</summary>
  
`python "autopy-downloader.py" -s "https://www.google.com/chrome/thank-you.html?statcb=1&standalone=1&platform=win&defaultbrowser=1" -x "/html/body/div[3]/section[1]/div/div/div/div/div[4]/p/a"`
</details>

_Recomendação: Utilizar XPath completo._ <br>
_Nota: O programa tem a intenção de automatizar tarefas no navegador. Em suma ele entra em um site e clica nos elementos indicados pelo XPath._

