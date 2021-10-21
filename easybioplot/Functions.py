import os
import time
import base64

def about():
	return '\n\t\t\t   EasyBioPlot\n\nAuther:\tYC Liang\nEmail:\t1694822092@qq.com\nAddress:\tCollege of Life Science, Inner Mongolia University, China'

def documentation():
    return 'http://bioinfor.imu.edu.cn/rpctdoc/'

def title():
    return 'EasyBioPlot: A tool for drawing pictures of biology'

def detal_time():
    return time.asctime(time.localtime(time.time()))

def command_str(li):
    out = ''
    for i in range(12-li):
        out += ' '
    return out

def save(command, file_path):
    with open(os.path.join(os.path.join(file_path, 'bin'), 'Logs.txt'),'a', encoding='UTF-8') as f:
        f.write('\n' + command)

def load(file_path):
    if 'bin' not in os.listdir(file_path):
        os.makedirs(os.path.join(file_path, 'bin'))
        os.makedirs(os.path.join(file_path, 'data'))
        content1 = 'AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAABILAAASCwAAAAAAAAAAAAD////////////////////////////////////////////////+/fv//fr0//369f/9+vX/+OrQ/9yXFf/clRL/3JUS/9yXFv/46tH//fr1//369f/9+vT//v37/////////////////////////////////////////////////////////////////////////////////////////v3//v37//LZqf/fnyb/36It/9+iLf/eoCn/25YS/9uWEv/blhL/25YS/96gKf/foi3/36Es/9+fJv/y2an//v37///+/f///////////////////////////////////////////////////////////////////////////+/Slf/gpTD/3qAo/9uVD//blRD/25UQ/9uVEf/blhL/25YS/9uWEv/blhL/25UR/9uVEP/blRD/25UP/96gKP/fozD/7tCV///////////////////////////////////////////////////////////////////////uzpH/3p0i/9qUDf/blRD/25YS/9uWEv/blhL/25YR/9qUDv/akw7/2pQO/9uUDv/blhH/2pQP/9uVEf/blhL/25UQ/9qUDf/dnSL/7s6R////////////////////////////////////////////////////////////7s2O/96eJP/alA7/25YS/9uWEv/blhL/25UQ/9qSC//foi7/9eG8//Xiv//147//9eG8/9+iLf/w05v/46xE/9qUDv/blhL/25YS/9qUDv/dniT/7c2O/////////////////////////////////////////////////+7Njv/eniT/2pQN/9uWEv/blhL/25YS/9qUDv/iqkD/7s2O/+CmOP//////////////////////4ac4//nu2f/mtlr/25MM/9uUDf/alA7/25YS/9qUDf/eniX/7s2O///////////////////////////////////////uzpH/3p4k/9qUDf/blhP/2pQN/9qUDf/blhL/2pMM/+a1WP/47NT/4KU3//79+/////////////79+//hpzf/5rdb/9+iLf/akwv/6b5t/+WzVf/ZkQj/25YS/9qUDf/eniT/7s6R/////////////////////////v3/7s+U/92dIv/alA7/25YS/9mRCP/ltFf/5bZa/9qUDf/alAz/5bRW//fpzv/gpTf//v37/////////////v37/+CnOP/Zkgn/25UQ/9mSCv/y2an/9+jM/+SwTv/akQj/25YS/9qUDv/dnSL/7s+U///+/f/////////////////fozH/2pQN/9uWEv/akgn/5LBN//fpzv/v0pr/2ZEJ/9qUDP/ltFb/9+nO/+ClN//+/fv////////////+/fv/4KY3/9qVD//blhL/2ZIK//DVoP//////9+fJ/+SvTf/Zkgj/25YS/9qUDf/fpDH////////////+/fv/8tmp/96gKP/blRD/2pUP/+SwTP/36Mz//////+3NkP/Ykgn/2pQM/+W0Vv/36c7/4KU3//79+/////////////79+//hpjf/25UP/9uWEv/akgn/8dWg////////////9+jL/+OwS//blQ//25UQ/96gKP/y2an//v37//369P/fnyb/25UP/9uWEv/Zkgv/9N61////////////7c6R/9mSCf/alAz/5bRW//fpzv/gpTf//v37/////////////v37/+GmN//blQ//25YS/9qSCf/x1aD/////////////////9N60/9mRB//blhL/2pUP/92fJv/9+vT//fr1/9+hLf/blRD/25YS/9qSCP/z26/////////////uzpH/2ZIJ/9qUDP/ltFb/9+nO/+ClN//+/fv////////////+/fv/4aY3/9uVD//blhL/2pIJ//HVoP/////////////////25cX/4ak8/9uVEf/blRD/36Iu//78+f/9+vX/3qEt/9uVEP/blhH/4KUy//bkwf///////////+7Okf/Zkgn/2pQM/+W0Vv/36c7/4KU3//79+/////////////79+//hpjf/25UP/9uWEv/akgn/8dWg///////////////////////25ML/2pQO/9uVEf/enyf/9uXE//779v/foi3/25UQ/9qUDv/147//////////////////7s6R/9mSCf/alAz/5bRW//fpzv/gpTf//v37/////////////v37/+GmN//blQ//25YS/9qSCf/x1aD///////////////////////Xjv//alA7/25YS/9uWEv/alRD/+u/b/9+hKv/blRH/2pQO//Xjv//////////////////uzpH/2ZIJ/9qUDP/ltFb/9+nO/+ClN//+/fv////////////+/fv/4aY3/9uVD//blhL/2pIJ//HVoP//////////////////////9eO//9uUDv/blhL/25YS/9qVEv/cmhr/25YT/9uWEv/alA7/9eO//////////////////+7Okf/Zkgn/2pQM/+W0Vv/36c7/4KU3//79+/////////////79+//fpjj/2pQP/9uWEv/akgn/8dWg///////////////////////147//2pQO/9uWEv/blhL/25US/9yaGv/blhP/25YS/9qUDv/147//////////////////7s6R/9mSCf/alAz/5bRW//fpzv/fpTf//v37/////v/++/b//fny/9+lNv/ZlA//2ZUS/9mRCv/w0pr//vv1//779f/9+/X//vz5//Xiv//akw7/25YS/9uWEv/blRL/+u/b/9+hKv/blRH/2pQO//Xjv//////////////////uzpH/2ZIJ/9qUDP/ltFb/9+nO/9+lN//+/vz//fjw/+CoPP/doCz/2pcW/9mVEv/ZlRL/2pUR/92dIf/foiz/36Is/96fJf/qwnf/9uXF/9qVDv/blhL/25YS/9qVEv/++/b/36It/9uVEP/alA7/9eO//////////////////+7Okf/Zkgn/2pQM/+W0V//36c//36U3///+/P/89+7/3Jwi/9mUEP/ZlRL/2ZUS/9mVEv/ZlRL/2pUR/9uVEP/blRH/2pEI/+i6Y//25sX/2pQO/9uWEv/blhL/2pUQ//369f/foy3/25UQ/9uWEf/gozL/9uPB////////////7s6R/9mSCf/blhH/3Zwh/9+mOP/fpjj///78//z37v/cnSP/2ZUR/9mVEv/ZlRL/2ZUS/9mVEv/alhL/25YS/9qSC//mtVn/+vHg//blw//alA7/25UR/96fJ//25cT//fr1/9+iLf/blRD/25YS/9qRCP/z26/////////////tzI3/2JAF/9uWEv/alRH/2JIM/9+mOP///vz//Pfu/9ydI//ZlRH/2ZUS/9mVEv/ZlRL/2ZUS/9qUDv/ZkAX/5rdd//nv2//358j/4ak8/9uVEf/blRD/36Iu//78+f/9+vT/358n/9uVD//blhL/2pML//Tetf////////////nu2v/ovWv/2Y8E/9mSCv/XkAf/3qMx//7+/P/89+3/25kc/9iRCf/YkQr/2JEK/9iRCv/XjwT/6L5u//Pbrf/57tf///////TetP/ZkQf/25YS/9uVD//eoCf//fr0//79+//y2an/3qAo/9uVEP/blQ//5LBM//fozP////////////rw3f/w053/8NWg//DUn//y26////7+//78+P/x2Kf/8NWg//DVoP/w1aD/8NWg/+/Tnf/68N3////////////36Mv/5LBL/9uVD//blRD/3qAo//LZqf/+/fv////////////fozH/2pQN/9uWEv/akgn/5LBM//fnyf//////////////////////////////////////////////////////////////////////////////////////9+fJ/+SwTf/akgj/25YS/9qUDf/fpDH///////////////////79/+7PlP/dnSL/2pQO/9uWEv/Zkgj/5LFO//fnyP////////////////////////////////////////////////////////////////////////////fmyP/ksE7/2ZII/9uWEv/alA7/3Z0i/+7PlP///v3//////////////////////+7Okf/eniT/2pQN/9uWEv/Zkgj/5LBN//fnyf/////////////////////////////////////////////////////////////////358n/5LBN/9mRCP/blhL/2pQN/92eJP/uzpH//////////////////////////////////////+7Ojv/enyX/2pQN/9uWEv/akgn/5LBM//PcsP/z267/9uTC//////////////////////////////////bkwv/z267/89yw/+SwTP/akgn/25YS/9qUDf/eniX/7c2O/////////////////////////////////////////////////+7Njv/eniT/2pQO/9uWEv/blQ//2pML/9qRCP/gpDH/9eK///Xiv//147//9eO///Xjv//147//4KQy/9qSCP/akwv/2pUP/9uWEv/alA7/3p4k/+7Njv///////////////////////////////////////////////////////////+7Okf/enSL/2pQN/9uVEP/blhL/25YS/9uWEf/alA7/2pMO/9qUDv/alA7/2pQO/9qUDv/blhH/25YS/9uWEv/blRD/2pQN/92dIv/uzpH//////////////////////////////////////////////////////////////////////+/Slf/gpTD/3qAo/9uVD//blRD/25UQ/9uVEf/blhL/25YS/9uWEv/blhL/25UR/9uVEP/blRD/25UP/96gKP/fozD/7tCV//////////////////////////////////////////////////////////////////////////////79//79+//y2an/358m/+CiLf/foi3/3qAp/9uWEv/blhL/25YS/9uWEv/eoCn/36It/+CiLf/foCf/8tmp//79+////v3///////////////////////////////////////////////////////////////////////////////////////79+//9+vT//fr1//369f/46tD/3JcV/9yVEv/clRL/3JcW//jq0f/9+vX//fr1//369P/+/fv/////////////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='
        content2 = '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'
        with open(os.path.join(os.path.join(file_path, 'bin'), 'Logo.ico'), 'wb') as f:
            f.write(base64.b64decode(content1))
        with open(os.path.join(os.path.join(file_path, 'bin'), 'Title.gif'), 'wb') as f:
            f.write(base64.b64decode(content2))
        with open(os.path.join(os.path.join(file_path, 'bin'), 'Logs.txt'), 'w', encoding='UTF-8') as f:
            f.write('')

def description_weblogo_signle():
    return 'Description: Input a FASTA file with sequences of equal length.'

def description_weblogo_mulity():
    return 'Description: Input a folder of FASTA files with sequences of equal length.'

def description_reduce_mulity():
    return 'Description: Input a FASTA file with single sequence.'

def commands(function, fuc_dic):
    out = function + command_str(len(function))
    for key in fuc_dic:
        out += ' ' + key + ' ' + fuc_dic[key]
    return out