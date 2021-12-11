from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    
    
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only = True)

    def validate(self, attrs):
        #password1과 password2가 맞지않으면
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "비밀번호가 맞지 않습니다.","password2":"비밀번호가 맞지 않습니다."})
        return attrs
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            nickname = validated_data['nickname'],
        )
        return user
    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "email", "nickname","password","password2" )





