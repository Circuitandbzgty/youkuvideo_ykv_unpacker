目前优酷的.ykv封装的的格式有.ts(MPEG-TS).flv(FlashVideo).mp4(MPEG-4Part14)
独播和付费的节目可以拆分成MPEG-TS,不支持解密。优酷使用了自研的copyrightDRM保护,有点难对付。
m3u8加密方式与以往的不一样，是加密了MPEG-TS中的payload载荷。属于阿里云私有加密方式。
拆分出来的的文件需要自己合成。总比没拆分的时候打不开好。