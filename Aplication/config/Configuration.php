<?php

namespace Configuration;

class Configuration
{
    private $config_file;
    public function __construct()
    {
        $this->config_file = fopen('..\\Aplication\\config.cnn','r');
    }

    public function get_constants()
    {
        return json_decode($this->config_file);
    }

}