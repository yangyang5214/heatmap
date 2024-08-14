# heatmap

### install

- GD 

```
# download
https://www.cpan.org/modules/by-module/GD/

cd GD-2.83
perl ./Makefile.PL

make
(sudo) make install


# 验证
perl -MGD -e 'print $GD::VERSION'
```


- imagemagick

```
brew install imagemagick
yum install ImageMagick -y
```

- libgd

```
cd libgd-2.3.3
./configure
make

make check 
# issue 763
export TMPDIR=/tmp && make check

# if check FAIL x. then install x

make install
```

### Reference

https://avtanski.net/projects/gps/

https://www.cnblogs.com/buptzym/p/5236181.html