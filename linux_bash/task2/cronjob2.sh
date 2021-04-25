#! /bin/bash
touch $HOME/weather.json | curl "api.openweathermap.org/data/2.5/weather?q=Kyiv&appid=80a57ef6042ae42e51f79bfe1cd4c2d4" > $HOME/weather.json