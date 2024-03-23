#include<iostream>
#include <numbers>
#include <cmath>
using namespace std;

const auto pi = numbers::pi;
int fun1() {
    cout << "专用计算" << endl;
    cout << "请选择计算（输入对应数字）" << endl;
    cout << "1.频率 波长 带宽" << endl;
    cout << "2.Num＆dB换算" << endl;
    cout << "3.dBm mW W换算" << endl;
    cout << "4.dBm Vrms Vpk Vpp换算" << endl;
    cout << "5.空间功率密度及场强计算" << endl;
    cout << "6.VSWR S11 ＆ρ换算" << endl;
    cout << "7.级联噪声系数计算" << endl;
    cout << "8.噪声系数NF＆噪温Te换算" << endl;
    cout << "9.合路增益核算" << endl;
    cout << "10.定向耦合器耦合损耗核算" << endl;
    cout << "11.多普勒＆相对速度 换算" << endl;
    cout << "12.自由空间损耗计算" << endl;
    cout << "13.视距相关计算" << endl;
    cout << "14.系统EIRP值计算" << endl;
    cout << "15.系统G/T值计算" << endl;
    cout << "16.发射EIRP布阵数量求解" << endl;
    cout << "17.接收G/T布阵数量求解" << endl;
    int Op;
    cin >> Op;

    switch (Op) {
    case 1: {
        cout << "请选择计算（输入对应数字）" << endl;
        cout << "1.频率 波长" << endl;
        cout << "2.中心频率，绝对带宽，分数带宽" << endl;
        int Opp;
        cin >> Opp;
        switch (Opp) {
        case 1: {
            cout << "频率f(GHz):" << endl;
            double f;
            cin >> f;
            cout << "介电常数:" << endl;
            double E;
            cin >> E;
            auto lambdazhen = 300 / f;
            auto lambdajie = 300 / (f * sqrt(E));
            printf("真空波长:%.2fmm\n", lambdazhen);
            printf("介质波长:%.2fmm\n", lambdajie);
            cout << "波长倍数:" << endl;
            double X;
            cin >> X;
            auto Xlamdazhen = 300 * X / f;
            auto Xlamdajie = 300 * X / (f * sqrt(E));
            printf("X倍真空波长:%.2fmm\n", Xlamdazhen);
            printf("X倍真空波长:%.2fmm\n", Xlamdajie);
        }
        case 2: {
            cout << "低频:" << endl;
            double Fl;
            cin >> Fl;
            cout << "高频:" << endl;
            double Fh;
            cin >> Fh;
            while (true) {
                if (Fl > Fh) {
                    printf("fl>fh,error!\n");
                    break;
                }
                auto Fc = (Fl + Fh) / 2;
                auto Bjue = Fh - Fl;
                auto Bbai = (Fh - Fl) * 100 / Fc;
                auto beipin = Fh / Fl;
                printf("中心频率:%f\n", Fc);
                printf("绝对带宽:%f\n", Bjue);
                printf("百分带宽:%.2f\n", Bbai);
                printf("倍频程:%.2f\n", beipin);
            }
        }
        default:
            break;
        }
    }
    case 2: {
        printf("请选择计算（输入对应数字）\n");
        printf("1.Num-->dB\n");
        printf("2.dB-->Num\n");
        int Opp;
        cin >> Opp;
        switch (Opp) {
        case 1: {
            cout << "Num:" << endl;
            double Num;
            cin >> Num;
            auto dB = 10 * log10(Num);
            printf("dB:%.2fdB\n", dB);
        }
        case 2: {
            cout << "dB:" << endl;
            double dB;
            cin >> dB;
            auto Num = pow(10, dB / 10);
            printf("Num:%.2f\n", Num);
        }
        default:
            break;
        }
    default:
        break;
    }
    case 3: {
        cout << "请选择计算（输入对应数字）" << endl;
        cout << "1.dBm-->W" << endl;
        cout << "2.dBW-->kW" << endl;
        cout << "3.mW-->dBm" << endl;
        cout << "4.mW-->dBW" << endl;
        cout << "5.W-->dBm" << endl;
        cout << "6.W-->dBW" << endl;
        cout << "7.dBm累加计算" << endl;
        int Opp;
        cin >> Opp;
        switch (Opp) {
        case 1: {
            cout << "功率分贝值dBm:" << endl;
            double dBm;
            cin >> dBm;
            auto W = pow(10, dBm / 10) / 1000;
            printf("功率十进制:%.2fW\n", W);
        }
        case 2: {
            cout << "功率分贝值dBW:" << endl;
            double dBW;
            cin >> dBW;
            auto kW = pow(10, dBW / 10) / 1000;
            printf("功率十进制:%.2fkW\n", kW);
        }
        case 3: {
            cout << "功率十进制mW:" << endl;
            double mW;
            cin >> mW;
            auto dBm = 10 * log10(mW);
            printf("功率分贝值:%.2fdBm\n", dBm);
        }
        case 4: {
            cout << "功率十进制mW:" << endl;
            double mW;
            cin >> mW;
            auto dBW = 10 * log10(mW / 1000);
            printf("功率分贝值:%.2fdBW\n", dBW);
        }
        case 5: {}
        case 6: {
            cout << "功率十进制W:" << endl;
            double W;
            cin >> W;
            auto dBW = 10 * log10(W);
            printf("功率分贝值:%.2fdBW\n", dBW);
        }
        case 7: {
            cout << "功率1(dBm):" << endl;
            double P1;
            cin >> P1;
            cout << "功率1(dBm):" << endl;
            double P2;
            cin >> P2;
            auto P = 10 * log10(pow(10, P1 / 10) + pow(10, P2 / 10));
            printf("合计功率:%.2fdBm\n", P);
        }
        }
    }
    case 4: {
        cout << "请选择计算（输入对应数字）" << endl;
        cout << "1.阻抗，功率" << endl;
        cout << "2.阻抗，有效电压" << endl;
        int Opp;
        cin >> Opp;
        switch (Opp) {
        case 1: {
            cout << "阻抗(Ω):" << endl;
            double R;
            cin >> R;
            cout << "功率(dBm):" << endl;
            double P;
            cin >> P;
            auto Vrms = sqrt(pow(10, P / 10) * R / 1000);
            auto Vpk = sqrt(2) * Vrms;
            auto Vpp = 2 * sqrt(2) * Vrms;
            printf("有效电压(Vrms):%.2fV\n", Vrms);
            printf("峰值电压(Vpk):%.2fV\n", Vpk);
            printf("峰峰电压(Vpp):%.2fV\n", Vpp);
        }
        case 2: {
            cout << "阻抗(Ω):" << endl;
            double R;
            cin >> R;
            cout << "有效电压(V):" << endl;
            double Vrms;
            cin >> Vrms;
            auto Vpk = sqrt(2) * Vrms;
            auto  Vpp = 2 * sqrt(2) * Vrms;
            auto  P = 10 * log10(1000 * pow(Vrms, 2) / R);
            printf("峰值电压(Vpk):%.2fV\n", Vpk);
            printf("峰峰电压(Vpp):%.2fV\n", Vpp);
            printf("功率(P):%.2fdBm\n", P);
        }
        }
    }
    case 5: {
        cout << "输入发射功率、发射天线增益或直接输入发射EIRP" << endl;
        cout << "请选择计算（输入对应数字）" << endl;
        cout << "1.输入发射功率、发射天线增益" << endl;
        cout << "2.直接输入发射EIRP" << endl;
        int Opp;
        cin >> Opp;
        switch (Opp) {
        case 1: {
            cout << "发射功率(dBm):" << endl;
            double P;
            cin >> P;
            cout << "发射天线增益(dB):" << endl;
            double G;
            cin >> G;
            cout << "空间距离(m):" << endl;
            double d;
            cin >> d;
            auto Pt = 10 * log10(pow(10, (P + G) / 10) / (4 * pi * pow(d, 2)));
            auto E = sqrt(120 * pi * (pow(10, (P + G) / 10) / (4000 * pi * pow(d, 2))));
            printf("功率密度:%.2fdBm/m^2\n", Pt);
            printf("场强:%.2fV/m^2\n", E);
        }
        case 2: {
            cout << "等效发射EIRP(dBm):" << endl;
            double EIRP;
            cin >> EIRP;
            cout << "空间距离(m):" << endl;
            double d;
            cin >> d;
            auto Pt = 10 * log10(pow(10, EIRP / 10) / (4 * pi * pow(d, 2)));
            auto E = sqrt(120 * pi * (pow(10, EIRP / 10) / (4000 * pi * pow(d, 2))));
            printf("功率密度:%.2fdBm/m^2\n", Pt);
            printf("场强:%.2fV/m^2\n", E);
        }
        }
    }
    }
    return 0;
}

int main() {
    fun1();
    system("pause");
}