
## 怎麼使用
大部分的設定都在 `templates\profile.yml`, 少部份需要在 `templates\template.html` 裡直接修改.  

### 安裝必要套件
```
sudo -H pip install jinja2
sudo -H pip install pyyaml
```

### 產生html
```
make
```

開啟 `dist\index.html`, 看輸出結果.  

### 佈署到 github
執行下列指令進行佈署, 會執行 `git subtree push --prefix dist origin gh-pages`  
將 dist 資料夾底下的東西推到遠端 gh-pages 分支上  
```
make deploy
```